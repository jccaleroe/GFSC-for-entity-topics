import argparse
import os

import spacy
import unidecode
from langdetect import detect
from tika import parser as tp

parser = argparse.ArgumentParser(
    description='Extract some named entities and some parts of speech from a corpus of document. Returns a folder per '
                'entity with only the recognized words per document. If all the files are plain text, omit the option '
                '--use_tika')
parser.add_argument('dataset', type=str, help='Folder with the corpus')
parser.add_argument('target', type=str, help='Folder to save entities')
parser.add_argument('--use_spanish', action='store_true', help='Use Spanish entities')
parser.add_argument('--use_tika', action='store_true', help='Use Spanish entities')
args = parser.parse_args()

print('loading spaCy')
if args.use_spanish:
    prefixes = {"VERB": "VERB", "ADJ": "ADJ", "PER": "PER", "LOC": "LOC", "ORG": "ORG", "NOUN": "NOUN"}
    nlp = spacy.load("es_core_news_lg")
    lang = 'es'
else:
    prefixes = {"PERSON": "PERSON", "NORP": "ORG", "ORG": "ORG", "LOC": "LOC", "FAC": "LOC", "GPE": "LOC",
                "PRODUCT": "OBJ",
                "WORK_OF_ART": "OBJ", "LAW": "OBJ", "EVENT": "EVENT", "VERB": "VERB", "ADJ": "ADJ", "NOUN": "NOUN"}
    nlp = spacy.load("en_core_web_lg")
    lang = 'en'

print('spaCy loaded')

types = set(prefixes.values())
for folder in types:
    os.makedirs(os.path.join(args.target, folder), exist_ok=True)

cnt = 0
for filename in os.listdir(args.dataset):
    if args.use_tika:
        s = tp.from_file(os.path.join(args.dataset, filename), requestOptions={'timeout': 300})['content']
    else:
        with open(os.path.join(args.dataset, filename), 'r') as f:
            s = f.read()
    s = '' if s is None else s.strip()
    if len(s) <= 40 or len(s) > 1000000:
        continue
    try:
        if detect(s) != lang:
            continue
    except:
        continue
    doc = nlp(s)
    cnt += 1

    writers = {}
    for folder in types:
        writers[folder] = open(os.path.join(args.target, folder, filename + '.txt'), 'w')

    for token in doc:
        if token.pos_ in prefixes:
            writers[prefixes[token.pos_]].write(unidecode.unidecode(token.lemma_.strip()).replace(' ', 'xyz') + '\n')

    for ent in doc.ents:
        if ent.label_ in prefixes:
            writers[prefixes[ent.label_]].write(unidecode.unidecode(ent.text.strip()).replace(' ', 'xyz') + '\n')

    for writer in writers.values():
        writer.close()

print(cnt, 'files processed')
