import os

import spacy
import unidecode

dataset = "/home/juan/Downloads/profiles/"
target = "/home/juan/adeline/artemis/hlta/datasets/profiles/"

os.makedirs(target + "verb/", exist_ok=True)
os.makedirs(target + "adj/", exist_ok=True)
os.makedirs(target + "per/", exist_ok=True)
os.makedirs(target + "loc/", exist_ok=True)
os.makedirs(target + "org/", exist_ok=True)

nlp = spacy.load("es_core_news_lg")
print('spaCy loaded')

for filename in os.listdir(dataset):
    with open(os.path.join(dataset, filename), 'r') as f:
        doc = nlp(f.read())
    print("processing " + filename)

    verb = open(target + "verb/" + filename, 'w')
    adj = open(target + "adj/" + filename, 'w')
    per = open(target + "per/" + filename, 'w')
    loc = open(target + "loc/" + filename, 'w')
    org = open(target + "org/" + filename, 'w')

    for token in doc:
        if token.pos_ == 'VERB':
            verb.write(unidecode.unidecode(token.lemma_.strip()).replace(' ', 'zzz') + '\n')
        elif token.pos_ == 'ADJ':
            adj.write(unidecode.unidecode(token.lemma_.strip()).replace(' ', 'zzz') + '\n')

    for i in doc.ents:
        if i.label_ == 'ORG':
            org.write(unidecode.unidecode(i.text.strip()).replace(' ', 'zzz') + '\n')
        elif i.label_ == 'LOC':
            loc.write(unidecode.unidecode(i.text.strip()).replace(' ', 'zzz') + '\n')
        elif i.label_ == 'PER':
            per.write(unidecode.unidecode(i.text.strip()).replace(' ', 'zzz') + '\n')

    verb.close()
    adj.close()
    per.close()
    loc.close()
    org.close()
