import os

import spacy

nlp = spacy.load("es_core_news_md")
print('spaCy loaded')

with open("profiles/adriana-cordoba.txt") as f:
    doc = nlp(f.read())

for i in doc.ents:
    print(i.label_ + "\t" + i.text)

# for token in doc:
#     print(token.pos_ + "\t" + token.lemma_)
