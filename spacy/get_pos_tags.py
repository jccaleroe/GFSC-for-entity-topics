import os

import spacy

nlp = spacy.load("es_core_news_md")
print('spaCy loaded')
dataset = "abstracts"

os.makedirs(dataset + "_verb/", exist_ok=True)
os.makedirs(dataset + "_propn/", exist_ok=True)
os.makedirs(dataset + "_num/", exist_ok=True)
os.makedirs(dataset + "_noun/", exist_ok=True)
os.makedirs(dataset + "_adj/", exist_ok=True)

for root, dirs, files in os.walk(dataset, topdown=False):
    for file in files:
        with open(dataset + "/" + file) as f:
            doc = nlp(f.read())

        verb = open(dataset + "_verb/" + file, 'w')
        propn = open(dataset + "_propn/" + file, 'w')
        num = open(dataset + "_num/" + file, 'w')
        noun = open(dataset + "_noun/" + file, 'w')
        adj = open(dataset + "_adj/" + file, 'w')

        for token in doc:
            if token.pos_ == 'VERB':
                verb.write(token.lemma_ + '\n')
            elif token.pos_ == 'PROPN':
                propn.write(token.lemma_ + '\n')
            elif token.pos_ == 'NUM':
                num.write(token.lemma_ + '\n')
            elif token.pos_ == 'NOUN':
                noun.write(token.lemma_ + '\n')
            elif token.pos_ == 'ADJ':
                adj.write(token.lemma_ + '\n')

        verb.close()
        propn.close()
        num.close()
        adj.close()
        noun.close()
