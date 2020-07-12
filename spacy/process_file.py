import spacy

# nlp = spacy.load("en_core_web_lg")
nlp = spacy.load("es_core_news_lg")
print('spaCy loaded')

with open("/home/juan/Downloads/profiles/Adriana  Córdoba") as f:
    doc = nlp(f.read())

for i in doc.ents:
    print(i.label_ + "\t" + i.text)

for token in doc:
    print(token.pos_ + "\t" + token.lemma_)
