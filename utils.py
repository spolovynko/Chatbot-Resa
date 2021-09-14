import spacy

def tokenize(text):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    return doc

def lemmatizer(doc):
    return [token.lemma_ for token in doc]


def remove_stopwords(doc):
    stopwords = spacy.lang.en.stop_words.STOP_WORDS
    return [token for token in doc if not token in stopwords]