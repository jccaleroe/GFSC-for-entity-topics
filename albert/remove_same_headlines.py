d = {}
with open('sarcasm_headlines/test_spanish.tsv') as f:
    f.readline()
    for i in f:
        tmp = i.split('\t')
        d[tmp[1][:-1]] = tmp[0]

print(len(d))
print(d['Es mejor que digan cosas malas sobre ti, a que no digan nada'])
with open('sarcasm_headlines/all2.tsv', 'w') as f:
    for i in d:
        f.write(d[i])
        f.write('\t')
        f.write(i)
        f.write('\n')