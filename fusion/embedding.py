import csv
import json
from collections import deque

import numpy as np


def load_nodes(name):
    n_trees = 0
    for prefix in prefixes:
        with open(name + prefix + '/topicTree.nodes.json', 'r') as read_file:
            j_nodes = json.load(read_file)
        q = deque()
        for node in j_nodes:
            node_parent[prefix + node['id']] = {'ROOT'}
            q.append(node)
            n_trees += 1
        while len(q) > 0:
            node = q.popleft()
            node_id = prefix + node['id']
            nodes[node_id] = len(nodes)
            node_words[node_id] = node['text'].split(' ')
            level = node['data']['level']
            node_level[node_id] = level
            if level not in nodes_per_level:
                nodes_per_level[level] = {}
                id2node[level] = {}
            nodes_per_level[level][node_id] = len(nodes_per_level[level])
            id2node[level][nodes_per_level[level][node_id]] = node_id
            node_children[node_id] = set()
            for child in node['children']:
                child_id = prefix + child['id']
                node_parent[child_id] = {node_id}
                node_children[node_id].add(child_id)
                q.append(child)
    print(n_trees, ' trees found')
    print(len(nodes), ' topics found')
    for level in nodes_per_level:
        print(len(nodes_per_level[level]), 'topics in level', level)


def load_assignments(name):
    for prefix in prefixes:
        with open(name + prefix + '/myAssignment.topics.json', 'r') as read_file:
            j_nodes = json.load(read_file)
        for node in j_nodes:
            topic = node['topic']
            assignments[prefix + topic] = {}
            for doc in node['doc']:
                assignments[prefix + topic][int(doc[0])] = doc[1]


def load_data_files(name):
    cnt = 0
    with open(name + 'myData.files.txt', 'r') as read_file:
        tmp = read_file.read().split('\n')
    for i in tmp:
        if len(i) == 0:
            continue
        data_files[cnt] = i
        cnt += 1


def load_words(name):
    repeated = {}
    for prefix in prefixes:
        with open(name + prefix + '/myData.dict.csv', 'r') as read_file:
            for tfidf in csv.reader(read_file):
                if tfidf[3] != 'tfidf':
                    if tfidf[0] not in words_dic:
                        words_dic[tfidf[0]] = len(words_dic)
                        tf_idf[tfidf[0]] = float(tfidf[3])
                    else:
                        if tfidf[0] not in repeated:
                            repeated[tfidf[0]] = 2
                        else:
                            repeated[tfidf[0]] += 1
                        tf_idf[tfidf[0]] += float(tfidf[3])
    for word in repeated:
        tf_idf[word] /= repeated[word]
    print(len(repeated), 'repeated words')


def load_sparse(name):
    with open(name + '/myData.sparse.txt', 'r') as read_file:
        doc_words = read_file.read().split('\n')
    for i in data_files:
        sparse[i] = []
    for i in doc_words:
        if len(i) == 0:
            continue
        tmp = i.split(", ")
        sparse[int(tmp[0])].append(tmp[1])


def read_java_bayes(name):
    for node in nodes:
        words_prop[node] = {}
    for prefix in prefixes:
        with open(name + prefix + '/myModel.bif', 'r') as f:
            for i in f:
                if i.count('|') == 0:
                    continue
                if i.startswith('probability ( '):
                    a = i[i.index('"') + 1: i.index('|') - 2]
                    b = prefix + i[i.index('|') + 3: i.index(')') - 2]
                    prob = float(f.readline().split(' ')[1])
                    if a.startswith('Z'):
                        if b not in node_prob:
                            node_prob[b] = {}
                        a = prefix + a
                        node_prob[b][a] = prob
                    else:
                        if a in words_dic:
                            words_prop[b][a] = prob


def prob_dfs(node):
    for child in node_children[node]:
        words = prob_dfs(child)
        for word in words:
            words_prop[node][word] = node_prob[node][child] * words_prop[child][word]
    return words_prop[node]


def get_words_prop(name):
    read_java_bayes(name)
    for node in nodes:
        if 'ROOT' in node_parent[node]:
            prob_dfs(node)


def save_np(folder, matrix, view_id):
    m_min = matrix.min()
    m_max = matrix.max()
    matrix -= m_min
    matrix /= (m_max - m_min)
    matrix *= 2
    matrix -= 1
    with open(folder + view_id + ".npy", 'wb') as f:
        np.save(f, matrix)


def get_files_view(path, level):
    nodes_number = len(nodes_per_level[level])
    view_files = np.zeros((nodes_number, len(data_files)))
    for node, node_id in nodes_per_level[level].items():
        for file in assignments[node]:
            view_files[node_id][file] = assignments[node][file]
    save_np(path, view_files, 'files')


def get_bayes_view(path, level):
    nodes_number = len(nodes_per_level[level])
    view_bayes = np.zeros((nodes_number, len(words_dic)))
    for node, node_id in nodes_per_level[level].items():
        for word in words_prop[node]:
            view_bayes[node_id][words_dic[word]] = words_prop[node][word]
    save_np(path, view_bayes, 'bayes')


def get_tfidf_view(path, level):
    nodes_number = len(nodes_per_level[level])
    view_tfidf = np.zeros((nodes_number, len(words_dic)))
    for node, node_id in nodes_per_level[level].items():
        for doc in assignments[node]:
            for word in sparse[doc]:
                if word in tf_idf:
                    view_tfidf[node_id][words_dic[word]] = tf_idf[word] * assignments[node][doc]
    save_np(path, view_tfidf, 'tfidf')


def get_views(name):
    import os
    folder = 'views/' + name + '/level_'
    for level in nodes_per_level:
        path = folder + str(level) + '/'
        os.makedirs(path, exist_ok=True)
        print("Getting views of level", level)
        get_files_view(path, level)
        get_bayes_view(path, level)
        get_tfidf_view(path, level)


def read_results(name):
    with open(name, 'rb') as f:
        return np.load(f)


def run_by_levels(clusters, name):
    import os
    for level in next(os.walk(clusters))[1]:
        process_clusters(read_results(clusters + level + '/' + name), int(level[-1]))
        print(len(nodes), 'nodes after fusion')


def create_node(u_name, cluster, c_id, level):
    nodes[u_name] = len(node_words)
    node_group[u_name] = c_id
    node_children[u_name] = set()
    node_parent[u_name] = set()
    for node_id in cluster:
        node = id2node[level][node_id]
        for parent in node_parent[node]:
            node_parent[u_name].add(parent)
            if parent != 'ROOT':
                if node in node_children[parent]:
                    node_children[parent].remove(node)
                node_children[parent].add(u_name)
        for child in node_children[node]:
            node_children[u_name].add(child)
            if node in node_parent[child]:
                node_parent[child].remove(node)
            node_parent[child].add(u_name)
        if level == 1:
            node_children[u_name].add(node)
            node_parent[node] = {u_name}
            node_group[node] = c_id
        else:
            del nodes[node]
            del node_children[node]
            del node_parent[node]
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


def process_clusters(labels, level):
    print('processing level', level)
    clusters = {}
    for i in range(len(labels)):
        if labels[i] in clusters:
            clusters[labels[i]].append(i)
        else:
            clusters[labels[i]] = [i]
    cnt = 0
    for c_id in clusters:
        if len(clusters[c_id]) == 1:
            node_group[id2node[level][clusters[c_id][0]]] = c_id
            continue
        create_node('U_' + str(level) + '_' + str(cnt), clusters[c_id], c_id, level)
        cnt += 1


def export_nodes_json(name):
    graph = []
    for node in nodes:
        entry = {'id': node, 'text': ' '.join(node_words[node]), 'children': []}
        graph.append(entry)
    with open(name, 'w') as f:
        json.dump(graph, f, indent=2)


def create_topics_d3(name, expanded):
    graph = {"nodes": {}, "links": []}
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
    with open("graphs/d3/" + name + '.json', "w") as fp:
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
    import os
    os.makedirs('graphs/gephi/', exist_ok=True)
    with open('graphs/gephi/' + name + '.gml', 'w') as f:
        f.write('\n'.join(graph))


# prefixes = ['PER', 'VERB', 'ORG', 'LOC', 'ADJ', 'NOUN']
prefixes = ['NOUN', 'LOC', 'VERB', 'ADJ', 'EVENT', 'OBJ', 'ORG', 'PERSON']
nodes, words_dic, node_words = {}, {}, {}
node_parent, node_level, node_children, nodes_per_level = {}, {}, {}, {}
id2node, node_group, data_files, assignments, tf_idf = {}, {}, {}, {}, {}
node_prob, words_prop, sparse = {}, {}, {}
dataset = 'organisms/'
load_nodes(dataset)
load_assignments(dataset)
load_data_files(dataset + 'NOUN/')
load_words(dataset)
get_words_prop(dataset)
load_sparse(dataset)
# get_views(dataset)
#run_by_levels('clusters/' + dataset, 'labels.npy')
export_nodes_json('organisms/evaluation/simple.organisms.nodes.json')
create_topics_gephi('simple.organisms')
create_topics_d3("simple.organisms", False)

