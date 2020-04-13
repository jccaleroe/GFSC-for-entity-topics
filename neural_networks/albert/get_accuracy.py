l = []
with open('sarcasm_headlines/test.tsv') as f:
    f.readline()
    for i in f:
        tmp = i.split('\t')
        l.append(tmp)

l2 = []
with open('sarcasm_results/bert_base/test_results.tsv') as f:
    for i in f:
        tmp = i.split('\t')
        if float(tmp[0]) > float(tmp[1]):
            l2.append(0)
        else:
            l2.append(1)

oks = 0.0
for i in range(len(l)):
    if float(l[i][0]) == l2[i]:
        oks += 1
    else:
        print('Failed in:', l[i][1], 'Expected:', l[i][0])

print('\nAccuracy:', oks / len(l))
print('Failed in', len(l) - oks, 'cases of', len(l), 'headlines')
