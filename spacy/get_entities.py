import os
import sys

import spacy
import unidecode

if len(sys.argv) != 4:
    # dataset = "/home/juan/Documents/profiles/"
    # target = "/home/juan/adeline/artemis/hlta/datasets/profiles/"

    dataset = "/home/juan/Downloads/new_life/"
    target = "/home/juan/adeline/artemis/hlta/datasets/organisms/"
    is_english = True
else:
    dataset = sys.argv[1]
    target = sys.argv[2]
    is_english = sys.argv[3] == "True"

if is_english:
    prefixes = {"PERSON": "PERSON", "NORP": "ORG", "ORG": "ORG", "LOC": "LOC", "FAC": "LOC", "GPE": "LOC",
                "PRODUCT": "OBJ",
                "WORK_OF_ART": "OBJ", "LAW": "OBJ", "EVENT": "EVENT", "VERB": "VERB", "ADJ": "ADJ", "NOUN": "NOUN"}
    nlp = spacy.load("en_core_web_lg")
else:
    prefixes = {"VERB": "VERB", "ADJ": "ADJ", "PER": "PER", "LOC": "LOC", "ORG": "ORG", "NOUN": "NOUN"}
    nlp = spacy.load("es_core_news_lg")
print('spaCy loaded')

types = set(prefixes.values())
for i in types:
    os.makedirs(target + i, exist_ok=True)

cnt = 0
for filename in os.listdir(dataset):
    with open(os.path.join(dataset, filename), 'r') as f:
        doc = nlp(f.read())
    cnt += 1

    writers = {}
    for i in types:
        writers[i] = open(target + i + '/' + filename, 'w')

    for token in doc:
        if token.pos_ in prefixes:
            writers[prefixes[token.pos_]].write(unidecode.unidecode(token.lemma_.strip()).replace(' ', 'xyz') + '\n')

    for ent in doc.ents:
        if ent.label_ in prefixes:
            writers[prefixes[ent.label_]].write(unidecode.unidecode(ent.text.strip()).replace(' ', 'xyz') + '\n')

    for writer in writers.values():
        writer.close()

print(cnt, 'files processed')
