import csv
import json
import os
from collections import deque


def load_nodes(name):
    n_trees = 0
    for prefix in prefixes:
        with open(os.path.join(name, prefix, 'topicTree.nodes.json'), 'r') as read_file:
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
        with open(os.path.join(name, prefix, 'myAssignment.topics.json'), 'r') as read_file:
            j_nodes = json.load(read_file)
        for node in j_nodes:
            topic = node['topic']
            assignments[prefix + topic] = {}
            for doc in node['doc']:
                assignments[prefix + topic][int(doc[0])] = doc[1]


def load_data_files(name):
    cnt = 0
    with open(os.path.join(name, 'myData.files.txt'), 'r') as read_file:
        tmp = read_file.read().split('\n')
    for i in tmp:
        if len(i) == 0:
            continue
        data_files[cnt] = i
        cnt += 1


def load_words(name):
    repeated = {}
    for prefix in prefixes:
        with open(os.path.join(name, prefix, 'myData.dict.csv'), 'r') as read_file:
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
    print(len(words_dic), ' unique words')
    print(len(repeated), 'repeated words')


def load_sparse(name):
    with open(os.path.join(name, 'myData.sparse.txt'), 'r') as read_file:
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
        with open(os.path.join(name, prefix, 'myModel.bif'), 'r') as f:
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


prefixes = []
nodes, words_dic, node_words = {}, {}, {}
node_parent, node_level, node_children, nodes_per_level = {}, {}, {}, {}
id2node, data_files, assignments, tf_idf = {}, {}, {}, {}
node_prob, words_prop, sparse = {}, {}, {}
