d = {}
with open('sarcasm_headlines/tmp') as f:
    for i in f:
        tmp = i.split('\t')
        d[tmp[1][:-1].lower()] = tmp[0]

print(len(d))
with open('sarcasm_headlines/tmp2.tsv', 'w') as f:
    for i in d:
        f.write(d[i])
        f.write('\t')
        f.write(i)
        f.write('\n')