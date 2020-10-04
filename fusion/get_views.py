import argparse
import os

import numpy as np

import embedding
from embedding import assignments
from embedding import data_files
from embedding import nodes_per_level
from embedding import sparse
from embedding import tf_idf
from embedding import words_dic
from embedding import words_prop


def save_np(folder, matrix, view_id):
    m_min = matrix.min()
    m_max = matrix.max()
    matrix -= m_min
    matrix /= (m_max - m_min)
    matrix *= 2
    matrix -= 1
    with open(os.path.join(folder, view_id + ".npy"), 'wb') as f:
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
    folder = os.path.join(name, 'level_')
    for level in nodes_per_level:
        path = folder + str(level)
        os.makedirs(path, exist_ok=True)
        print('Getting level', level, 'views')
        get_files_view(path, level)
        get_bayes_view(path, level)
        get_tfidf_view(path, level)


parser = argparse.ArgumentParser(
    description='Get hlta topic views from the folder specified. These topics must have certain '
                'conditions granted if the folder comes from the ../hlta/run_all.sh script.')
parser.add_argument('dataset', type=str, help='Folder with the topic models')
parser.add_argument('views_folder', type=str, help='Folder to save the views')
parser.add_argument('--use_spanish', action='store_true', help='Use Spanish entities')
args = parser.parse_args()

if args.use_spanish:
    embedding.prefixes = ['PER', 'VERB', 'ORG', 'LOC', 'ADJ', 'NOUN']
else:
    embedding.prefixes = ['NOUN', 'LOC', 'VERB', 'ADJ', 'EVENT', 'OBJ', 'ORG', 'PERSON']

embedding.load_nodes(args.dataset)
embedding.load_assignments(args.dataset)
embedding.load_data_files(args.dataset)
embedding.load_words(args.dataset)
embedding.get_words_prop(args.dataset)
embedding.load_sparse(args.dataset)
get_views(args.views_folder)
