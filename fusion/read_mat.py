import mat73
import numpy as np

d = mat73.loadmat('reuters_1200.mat')

print(len(d['labels']))
print(len(d['data']))

views = []

for i in d['data']:
    x = np.array(i[0])
    m = x.min()
    x -= m
    x /= (x.max() - m)
    x *= 2
    x -= 1
    views.append(x)

labels = np.array(d['labels'])

for i in range(len(views)):
    with open("reuters_views/view" + str(i) + ".npy", 'wb') as f:
        np.save(f, views[i])
    print(views[i])
    print('###########')

with open("reuters_views/labels.npy", 'wb') as f:
    np.save(f, labels)

print(labels)
