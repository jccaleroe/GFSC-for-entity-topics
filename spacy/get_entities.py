import os
import sys

import spacy
import unidecode
from langdetect import detect
from tika import parser

if len(sys.argv) != 5:
    print('Usage: dataset, target, is_english, use_tika')
    exit(1)

dataset = sys.argv[1]
target = sys.argv[2]
is_english = sys.argv[3] == "True"
use_tika = sys.argv[4] == "True"

print('loading spaCy')

if is_english:
    prefixes = {"PERSON": "PERSON", "NORP": "ORG", "ORG": "ORG", "LOC": "LOC", "FAC": "LOC", "GPE": "LOC",
                "PRODUCT": "OBJ",
                "WORK_OF_ART": "OBJ", "LAW": "OBJ", "EVENT": "EVENT", "VERB": "VERB", "ADJ": "ADJ", "NOUN": "NOUN"}
    nlp = spacy.load("en_core_web_lg")
    lang = 'en'
else:
    prefixes = {"VERB": "VERB", "ADJ": "ADJ", "PER": "PER", "LOC": "LOC", "ORG": "ORG", "NOUN": "NOUN"}
    nlp = spacy.load("es_core_news_lg")
    lang = 'es'

print('spaCy loaded')

types = set(prefixes.values())
for i in types:
    os.makedirs(target + i, exist_ok=True)

cnt = 0
for filename in os.listdir(dataset):
    if use_tika:
        s = parser.from_file(os.path.join(dataset, filename), requestOptions={'timeout': 300})['content']
    else:
        with open(os.path.join(dataset, filename), 'r') as f:
            s = f.read()
    s = '' if s is None else s.strip()
    if len(s) == 0 or len(s) > 1000000:
        continue
    try:
        if detect(s) != lang:
            continue
    except:
        continue
    doc = nlp(s)
    cnt += 1

    writers = {}
    for i in types:
        writers[i] = open(target + i + '/' + filename + '.txt', 'w')

    for token in doc:
        if token.pos_ in prefixes:
            writers[prefixes[token.pos_]].write(unidecode.unidecode(token.lemma_.strip()).replace(' ', 'xyz') + '\n')

    for ent in doc.ents:
        if ent.label_ in prefixes:
            writers[prefixes[ent.label_]].write(unidecode.unidecode(ent.text.strip()).replace(' ', 'xyz') + '\n')

    for writer in writers.values():
        writer.close()

print(cnt, 'files processed')

