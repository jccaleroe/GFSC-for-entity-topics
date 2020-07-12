import os

import spacy

dataset = "/home/juan/Downloads/profiles/"
target = "/home/juan/Downloads/profiles_nlp/"

os.makedirs(target + "verb/", exist_ok=True)
os.makedirs(target + "propn/", exist_ok=True)
os.makedirs(target + "noun/", exist_ok=True)
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
    propn = open(target + "propn/" + filename, 'w')
    noun = open(target + "noun/" + filename, 'w')
    adj = open(target + "adj/" + filename, 'w')
    per = open(target + "per/" + filename, 'w')
    loc = open(target + "loc/" + filename, 'w')
    org = open(target + "org/" + filename, 'w')

    for token in doc:
        if token.pos_ == 'VERB':
            verb.write(token.lemma_ + '\n')
        elif token.pos_ == 'INTJ':
            propn.write(token.lemma_ + '\n')
        elif token.pos_ == 'NOUN':
            noun.write(token.lemma_ + '\n')
        elif token.pos_ == 'ADJ':
            adj.write(token.lemma_ + '\n')

    for i in doc.ents:
        if i.label_ == 'ORG':
            org.write(i.text + '\n')
        elif i.label_ == 'LOC':
            loc.write(i.text + '\n')
        elif i.label_ == 'PER':
            per.write(i.text + '\n')

    verb.close()
    propn.close()
    adj.close()
    noun.close()
    per.close()
    loc.close()
    org.close()
