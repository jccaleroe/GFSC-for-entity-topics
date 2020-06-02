import mat73
import numpy as np

d = mat73.loadmat('reuters_1200.mat')

print(len(d['labels']))
print(len(d['data']))

views = []

for i in d['data']:
    matrix = np.array(i[0])
    m_min = matrix.min()
    m_max = matrix.max()
    matrix -= m_min
    matrix /= (m_max - m_min)
    matrix *= 2
    matrix -= 1
    views.append(matrix)

labels = np.array(d['labels'])

for i in range(len(views)):
    with open("reuters_views/view" + str(i) + ".npy", 'wb') as f:
        np.save(f, views[i])
    print(views[i])
    print('###########')

with open("reuters_views/labels.npy", 'wb') as f:
    np.save(f, labels)

print(labels)
