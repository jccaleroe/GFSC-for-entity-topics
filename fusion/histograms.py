import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics


def read_results(name):
    with open(name, 'rb') as f:
        return np.load(f)


def load_views(views_folder, level):
    views = {level: {}}
    for filename in os.listdir(os.path.join(views_folder, level)):
        with open(os.path.join(views_folder, level, filename), 'rb') as f:
            views[level][filename] = np.load(f)
    return views


def create_histograms(path, views_folder):
    histograms = {}
    for level in next(os.walk(path))[1]:
        labels = read_results(os.path.join(path, level, 'labels.npy'))
        # graph = read_results(os.path.join(path, level, 'graph.npy'))
        views = load_views(views_folder, level)
        print(level)
        for view in views[level]:
            print('Silhouette', view, round(metrics.silhouette_score(views[level][view], labels, metric='euclidean'), 4))
            print('Calinski-Harabasz', view, round(metrics.calinski_harabasz_score(views[level][view], labels), 4))
            print('Davies-Bouldin', view, round(metrics.davies_bouldin_score(views[level][view], labels), 4))
        d = {}
        for i in labels:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        big, small = float('-inf'), float('inf')
        for i in d:
            big = max(big, d[i])
            small = min(small, d[i])
        histograms[level] = [d, level + ', n: ' + str(len(labels)) + ', k: ' + str(len(d))
                             + ', Biggest: ' + str(big) + ', Smallest: ' + str(small)]
    return histograms


def plot_histograms(histograms):
    # plt.style.use('dark_background')
    plt.figure(figsize=(20, 30))
    plt.subplots_adjust(hspace=0.4)
    cnt = 1
    for h in histograms:
        plt.subplot(len(histograms), 1, cnt)
        cnt += 1
        d = histograms[h][0]
        plt.bar(d.keys(), d.values())
        plt.title(histograms[h][1], fontsize=30)
    plt.show()


plot_histograms(create_histograms("clusters/single_view/organisms/tfidf", 'views/organisms/tfidf'))
