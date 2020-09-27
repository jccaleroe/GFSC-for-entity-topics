import argparse
import os

import numpy as np
import tensorflow as tf
from sklearn.cluster import SpectralClustering


def load_data(path):
    x = None
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'rb') as f:
            tmp = tf.cast([np.load(f)], dtype=tf.float64)
            if x is None:
                x = tf.linalg.matmul(tmp, tmp, transpose_b=True)
            else:
                x = tf.concat([x, tf.linalg.matmul(tmp, tmp, transpose_b=True)], axis=0)
    return x


def fusion(x, k, steps, alpha, beta, gamma):
    n = x.shape[1]
    t = x.shape[0]
    reg = gamma / (4.0 * beta)
    wv, wv_u = tf.cast([1.0 / t for _ in range(t)], dtype=tf.float64), None
    i_alpha = tf.math.multiply(tf.eye(n, dtype=tf.float64), alpha)
    i_beta = tf.math.multiply(tf.eye(n, dtype=tf.float64), beta)
    s = tf.eye(n, dtype=tf.float64)
    for step in range(steps):
        s = tf.where(s > 0, s, tf.zeros(s.shape, dtype=tf.float64))
        s = tf.math.divide(tf.math.add(s, tf.transpose(s)), 2.0)
        z_sum = tf.zeros(s.shape, dtype=tf.float64)
        for i in range(t):
            z = tf.linalg.solve(
                tf.math.add(tf.math.add(x[i], i_alpha), tf.math.multiply(i_beta, wv[i])),
                tf.math.add(tf.math.multiply(s, tf.math.multiply(wv[i], beta)), x[i]))
            z = tf.where(z > 0, z, tf.zeros(z.shape, dtype=tf.float64))
            z = tf.math.divide(tf.math.add(z, tf.transpose(z)), 2.0)
            w = tf.math.divide(0.5, tf.norm(tf.math.subtract(z, s)))
            wv_u = tf.reshape(w, [1]) if i == 0 else tf.concat([wv_u, [w]], axis=0)
            z = tf.math.multiply(z, w)
            z_sum = tf.math.add(z_sum, z)
        (_, f) = tf.linalg.eigh(tf.math.subtract(tf.linalg.diag(tf.math.reduce_sum(s, 0)), s))
        f = tf.slice(f, [0, 0], [f.shape[0], k])
        p = tf.norm(tf.math.subtract(f[0][:], f), axis=1, keepdims=True)
        for i in range(1, n):
            p = tf.concat([p, tf.norm(tf.math.subtract(f[i][:], f), axis=1, keepdims=True)], 1)
        p = tf.math.multiply(tf.math.square(p), reg)
        wv = wv_u
        s_old = s
        s = tf.math.divide((tf.math.subtract(z_sum, p)), tf.math.reduce_sum(wv, 0))
        if step >= 4 and tf.math.less(tf.math.divide(tf.norm(tf.math.subtract(s, s_old)), tf.norm(s_old)), 1.e-3):
            return s.numpy()
    return s.numpy()


def run_clustering(k, x):
    return SpectralClustering(n_clusters=k, affinity='precomputed', assign_labels='discretize').fit(x).labels_


def save_np(folder, name, matrix):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, name) + ".npy", 'wb') as f:
        np.save(f, matrix)


def run(views):
    x = load_data(views)
    print(x.shape)
    steps, alpha, beta, gamma = 20, 0.1, 4000.0, 0.01
    k = max(4, int(x.shape[1] / 10))
    s = fusion(x, k, steps, alpha, beta, gamma)
    return k, s


def run_by_levels(views, clusters_folder):
    for level in next(os.walk(views))[1]:
        (k, s) = run(os.path.join(views, level))
        labels = run_clustering(k, s)
        save_np(os.path.join(clusters_folder, level), 'labels', labels)


parser = argparse.ArgumentParser(description='GFSC tensorflow and scikit-learn implementation which reads separately '
                                             'the numpy vectors stored on the path specified level-1 sub-folders '
                                             'and returns the clustering labels per sub-folder')
parser.add_argument('views_folder', type=str, help='Folder with the topic model views')
parser.add_argument('clusters_folder', type=str, help='Folder to save the topic clustering labels')
args = parser.parse_args()

run_by_levels(args.views_folder, args.clusters_folder)
