import spacy

def tokenize(text):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    return doc