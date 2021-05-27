import argparse
import json
import os

import numpy as np

import embedding
from embedding import id2node
from embedding import node_children
from embedding import node_parent
from embedding import node_words
from embedding import nodes
from embedding import node_level
from embedding import nodes_per_level


def read_results(name):
    if os.path.isfile(name):
        with open(name, 'rb') as f:
            return np.load(f)
    else:
        return []


def run_by_levels(clusters, name, omit_fusion):
    for level in next(os.walk(clusters))[1]:
        process_clusters(read_results(os.path.join(clusters, level, name)), int(level[-1]), omit_fusion)
        print(len(nodes), 'nodes after fusion')


def create_node(u_name, cluster, c_id, level):
    nodes[u_name] = len(node_words)
    node_group[u_name] = c_id
    node_level[u_name] = level
    node_children[u_name] = set()
    node_parent[u_name] = set()
    nodes_per_level[level][u_name] = nodes[u_name]
    fusion_parent = {}
    for node_id in cluster:
        node = id2node[level][node_id]
        for parent in node_parent[node]:
            if parent in fusion_parent:
                fusion_parent[parent] += 1
            else:
                fusion_parent[parent] = 1
            if parent != 'ROOT':
                if node in node_children[parent]:
                    node_children[parent].remove(node)
        for child in node_children[node]:
            node_children[u_name].add(child)
            if node in node_parent[child]:
                node_parent[child].remove(node)
            node_parent[child].add(u_name)
        if level == 1:
            node_children[u_name].add(node)
            node_parent[node] = {u_name}
            node_group[node] = c_id
            node_level[node] = 0
        else:
            del nodes[node]
            del node_children[node]
            del node_parent[node]
            del nodes_per_level[level][node]

    best_parent = 'ROOT'
    max_children = -1
    for parent in fusion_parent:
        if parent == 'ROOT':
            continue
        if fusion_parent[parent] > max_children:
            max_children = fusion_parent[parent]
            best_parent = parent
    node_parent[u_name].add(best_parent)
    if best_parent != 'ROOT':
        node_children[best_parent].add(u_name)

    node_words[u_name] = set()
    i = 0
    while True:
        no_more = True
        for node_id in cluster:
            node = id2node[level][node_id]
            if len(node_words[node]) > i:
                no_more = False
                if node_words[node][i] not in node_words[u_name]:
                    node_words[u_name].add(node_words[node][i])
                if len(node_words[u_name]) >= 7:
                    no_more = True
                    break
        if no_more:
            break
        i += 1


def process_clusters(labels, level, omit_fusion):
    print('processing level', level)
    clusters = {}
    for i in range(len(labels)):
        if labels[i] in clusters:
            clusters[labels[i]].append(i)
        else:
            clusters[labels[i]] = [i]
    cnt = 0
    for c_id in clusters:
        if omit_fusion:
            for node_id in clusters[c_id]:
                node_group[id2node[level][node_id]] = c_id
        else:
            if len(clusters[c_id]) == 1:
                node_group[id2node[level][clusters[c_id][0]]] = c_id
                continue
            create_node('U_' + str(level) + '_' + str(cnt), clusters[c_id], c_id, level)
            cnt += 1


def dfs_json(node):
    entry = {'id': node, 'text': ' '.join(node_words[node]), 'children': [],
             'data': {'level': node_level[node]}}
    if len(node_children[node]) == 0:
        return entry
    for child in node_children[node]:
        c_entry = dfs_json(child)
        entry['children'].append(c_entry)
    return entry


def export_nodes_json(name):
    graph = []
    for node in nodes:
        if node_parent[node] == {'ROOT'}:
            graph.append(dfs_json(node))
    with open(name + '.nodes.json', 'w') as f:
        json.dump(graph, f, indent=2)


def html_dfs(node):
    words = node if node.startswith('U') else node[:node.index('Z')]
    words = words + ': ' + ' '.join(node_words[node]).replace('xyz', '_')
    if len(node_children[node]) == 0:
        html.append('<li>' + words + '</li>')
    else:
        html.append('<li>' + words + '<ul>')
        for child in node_children[node]:
            html_dfs(child)
        html.append('</ul></li>')


def create_topics_html_lists(name):
    cnt = 0
    html.append('<style>.collapsibleList li {cursor: auto; margin: 8px 0;} li.collapsibleListOpen {cursor: pointer}')
    html.append('li.collapsibleListClosed {cursor: pointer}</style><script src="CollapsibleLists.js"></script>')
    html.append('<body onload="CollapsibleLists.apply();">')
    html.append('<ul class="collapsibleList">')
    for node in node_parent:
        if 'ROOT' in node_parent[node]:
            cnt += 1
            html_dfs(node)
            html.append('<br>')
    html.append('</ul></body>')
    os.makedirs('graphs/html', exist_ok=True)
    with open(os.path.join('graphs/html', name + '.html'), 'w') as f:
        f.write('\n'.join(html))
    print(cnt, "trees created")


def create_topics_d3(name, expanded):
    graph = {"nodes": {}, "links": []}
    if len(node_group) == 0:
        for i in nodes:
            node_group[i] = 0
    for node in nodes:
        words = node if node.startswith('U') else node[:node.index('Z')]
        words = words + ': ' + ' '.join(node_words[node]).replace('xyz', '_')
        is_root = False
        if 'ROOT' in node_parent[node]:
            is_root = True
        d = {"id": node, "name": words, "group": int(node_group[node]),
             "isRoot": expanded or is_root, "children": list(node_children[node]), "expanded": expanded}
        graph["nodes"][node] = d
        if expanded:
            for child in node_children:
                graph["links"].append((dict([('id', node + '-' + child), ("source", node), ("target", child)])))
    with open(os.path.join("graphs/d3", name + '.json'), "w") as fp:
        json.dump(graph, fp, indent=2)


def create_topics_gephi(name):
    colors = {}
    r, g, b, rr, gr, br, cnt = 80, 70, 60, 80, 70, 60, 0
    if len(node_group) == 0:
        for i in nodes:
            node_group[i] = 0
        colors[0] = '000000'
    else:
        for i in node_group.values():
            if i not in colors:
                color = '{:02x}'.format(r) if cnt < 4 else '00'
                color += '{:02x}'.format(g) if cnt % 2 == 0 else '00'
                color += '{:02x}'.format(b) if 1 < cnt < 6 else '00'
                cnt += 1
                if cnt == 7:
                    r = (r + rr) % 256
                    g = (g + gr) % 256
                    b = (b + br) % 256
                    cnt = 0
                colors[i] = color
    graph = ['graph [ directed 1']
    for node in nodes:
        words = node if node.startswith('U') else node[:node.index('Z')]
        words = words + ': ' + ' '.join(node_words[node]).replace('xyz', '_')
        graph.append('node [')
        graph.append('id ' + str(nodes[node]))
        graph.append('label "' + words + '"')
        graph.append('graphics [fill "#' + colors[node_group[node]] + '"]]')
    for node in nodes:
        for child in node_children[node]:
            graph.append('edge [')
            graph.append('source ' + str(nodes[node]))
            graph.append('target ' + str(nodes[child]) + ' ]')
    graph.append(']')
    os.makedirs('graphs/gephi/', exist_ok=True)
    with open(os.path.join('graphs/gephi', name + '.gml'), 'w') as f:
        f.write('\n'.join(graph))


parser = argparse.ArgumentParser(description='Process hlta topics on the folder specified with certain conditions '
                                             'granted if the folder comes from the ../hlta/run_all.sh script')
parser.add_argument('dataset', type=str, help='Folder with the topic models')
parser.add_argument('clusters_folder', type=str, help='Folder with the topic clustering labels')
parser.add_argument('--use_spanish', action='store_true', help='Use Spanish entities')
parser.add_argument('--gephi_name', type=str,
                    help='Process views and export as gml format into graphs/gephi/{gephi_name}')
parser.add_argument('--json_topics', type=str,
                    help='Process views and export nodes in json format without hierarchy into {dataset}/evaluation/{name}')
parser.add_argument('--d3_name', type=str,
                    help='Process views and export as json compatible with custom d3 visualizer into graphs/d3/{d3_name}')
parser.add_argument('--html_name', type=str,
                    help='Process views and export as HTML lists into graphs/html/{html_name}')
parser.add_argument('--omit_fusion', action='store_true', help='Join all topics in single json without fusion')
args = parser.parse_args()

if args.json_topics is None and args.gephi_name is None and args.d3_name is None and args.html_name is None:
    from sys import exit
    print('Must specify al least one action')
    exit(2)

if args.use_spanish:
    embedding.prefixes = ['PER', 'VERB', 'ORG', 'LOC', 'ADJ', 'NOUN']
else:
    embedding.prefixes = ['NOUN', 'LOC', 'VERB', 'ADJ', 'EVENT', 'OBJ', 'ORG', 'PERSON']

node_group = {}
embedding.load_nodes(args.dataset)
embedding.load_words(args.dataset)

run_by_levels(args.clusters_folder, 'labels.npy', args.omit_fusion)
if args.json_topics is not None:
    os.makedirs(os.path.join(args.dataset, 'evaluation'), exist_ok=True)
    export_nodes_json(os.path.join(args.dataset, 'evaluation', args.json_topics))
if args.gephi_name is not None:
    create_topics_gephi(args.gephi_name)
if args.d3_name is not None:
    create_topics_d3(args.d3_name, False)
if args.html_name is not None:
    html = []
    create_topics_html_lists(args.html_name)
