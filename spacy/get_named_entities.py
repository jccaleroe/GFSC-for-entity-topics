import os

import spacy

nlp = spacy.load("es_core_news_md", disable=["parser"])
print('spaCy loaded')
dataset = "abstracts"

os.makedirs(dataset + "_per/", exist_ok=True)
os.makedirs(dataset + "_loc/", exist_ok=True)
os.makedirs(dataset + "_misc/", exist_ok=True)
os.makedirs(dataset + "_org/", exist_ok=True)

for root, dirs, files in os.walk(dataset, topdown=False):
    for file in files:
        with open(dataset + file) as f:
            doc = nlp(f.read())

        per = open(dataset + "_per/" + file, 'w')
        loc = open(dataset + "_loc/" + file, 'w')
        misc = open(dataset + "_misc/" + file, 'w')
        org = open(dataset + "_org/" + file, 'w')

        for i in doc.ents:
            if i.label_ == 'MISC':
                misc.write(i.text + '\n')
            elif i.label_ == 'ORG':
                org.write(i.text + '\n')
            elif i.label_ == 'LOC':
                loc.write(i.text + '\n')
            elif i.label_ == 'PER':
                per.write(i.text + '\n')

        per.close()
        loc.close()
        misc.close()
        org.close()
