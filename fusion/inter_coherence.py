import argparse
import math

import embedding
from embedding import id2node
from embedding import node_children
from embedding import node_words
from embedding import nodes_per_level


def coherence(topic_a, topic_b):
    c = 0
    for word_a in node_words[topic_a]:
        for word_b in node_words[topic_b]:
            d_i_j = len(sparse[word_a].intersection(sparse[word_b]))
            u = len(sparse[word_a].union(sparse[word_b]))
            c += math.log((d_i_j + 1) / u)
    return c / (len(node_words[topic_a]) * len(node_words[topic_b]))


def append_to_text(text):
    f = open(export_file, 'a')
    f.write(text)
    f.close()


def parent_child_coherence():
    avg = cnt = 0
    for node in node_children:
        if len(node_children[node]) == 0:
            continue
        c = 0
        for child in node_children[node]:
            c += coherence(node, child)
        c /= len(node_children[node])
        avg += c
        cnt += 1
    avg = avg / cnt
    append_to_text('Parent-child topic coherence' + '\n' + str(avg) + '\n')


def inter_coherence():
    avg = 0
    append_to_text('Inter topic coherence' + '\n')
    for level in nodes_per_level:
        n = len(nodes_per_level[level])
        print('Calculating inter coherence of', n, 'topics on level', level)
        c = 0
        for i in range(n):
            for j in range(i + 1, n):
                c += coherence(id2node[level][i], id2node[level][j])
        c = c / (n * (n - 1) / 2)
        append_to_text('Level ' + str(level) + '\n' + str(c) + '\n')
        avg += c
    avg = avg / len(nodes_per_level)
    append_to_text('All levels average' + '\n' + str(avg) + '\n')


def load_word_sparse(name):
    with open(name, 'r') as read_file:
        doc_words = read_file.read().split('\n')
    word_doc = {}
    for i in doc_words:
        if len(i) == 0:
            continue
        tmp = i.split(", ")
        if tmp[1] not in word_doc:
            word_doc[tmp[1]] = set()
        word_doc[tmp[1]].add(int(tmp[0]))
    return word_doc


parser = argparse.ArgumentParser(description='Evaluate inter topics coherence')
parser.add_argument('topics', type=str, help='Topics on json format')
parser.add_argument('sparse', type=str, help='File with the dataset sparse')
parser.add_argument('export_file', type=str, help='File to export the results')
parser.add_argument('--inter_coherence', action='store_true', help='Use Spanish entities')
parser.add_argument('--parent_child_coherence', action='store_true', help='Use Spanish entities')
parser.add_argument('--all_metrics', action='store_true', help='Use Spanish entities')
args = parser.parse_args()

embedding.prefixes = ['']
embedding.topic_file = args.topics
embedding.load_nodes('')
sparse = load_word_sparse(args.sparse)
export_file = args.export_file
if args.inter_coherence or args.all_metrics:
    inter_coherence()
if args.parent_child_coherence or args.all_metrics:
    parent_child_coherence()
