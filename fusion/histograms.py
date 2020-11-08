import os

import matplotlib.pyplot as plt
import numpy as np


def read_results(name):
    with open(name, 'rb') as f:
        return np.load(f)


def create_histograms(path):
    histograms = {}
    for level in next(os.walk(path))[1]:
        labels = read_results(path + level + '/' + 'labels.npy')
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


plot_histograms(create_histograms("clusters/organisms/"))
