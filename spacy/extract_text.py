import os
import sys

from tika import parser

if len(sys.argv) != 3:
    print('Usage: dataset, target')
    exit(1)

dataset = sys.argv[1]
target = sys.argv[2]

cnt = 0
for filename in os.listdir(dataset):
    s = parser.from_file(os.path.join(dataset, filename), requestOptions={'timeout': 300})['content']
    s = '' if s is None else s.strip()
    if len(s) == 0:
        continue
    cnt += 1
    with open(os.path.join(target, filename + '.txt'), 'w') as f:
        f.write(s)

print(cnt, 'files processed')
