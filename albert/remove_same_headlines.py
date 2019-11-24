d = {}
with open('sarcasm_headlines/all.tsv') as f:
    f.readline()
    for i in f:
        tmp = i.split('\t')
        d[tmp[1][:-1]] = tmp[0]

print(len(d))
print(d['internet charmed by viral photo of teen working to pay for first real date'])
with open('sarcasm_headlines/all2.tsv', 'w') as f:
    for i in d:
        f.write(d[i])
        f.write('\t')
        f.write(i)
        f.write('\n')