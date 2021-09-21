from fuzzywuzzy import process
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import numpy as np



def tokenize(sentence, nlp):
    sentence = sentence.lower()
    sent = nlp(sentence)
    tokens = [token.lemma_ for token in sent if not token.is_stop]
    return tokens

def is_angry(sentence, nlp, model, tokenizer, max_len):
    sent = [token for token in tokenize(sentence, nlp)]
    print(sent)
    sent = [token[0]for token in tokenizer.texts_to_sequences(sent) if len(token)>0]
    sent = pad_sequences([sent], maxlen=max_len)
    return np.argmax(model(sent))==1


def typos_correction(sentence, dictionnary):
    punctuation = '.?!,;(){}[]<>\/#'
    for k in punctuation:
        sentence = sentence.replace(k, ' ')
    sentence = re.sub(r'( )+', ' ', sentence).lower()
    words = []
    for word in sentence.split(' '):
            fuzz_word, score = process.extractOne(word, dictionnary)
            if score>80:
                words.append(fuzz_word)
            else:
                words.append(word)
    return ' '.join(words)


if __name__ == '__main__':
    import spacy
    import pickle
    from tensorflow.keras.models import load_model
    import tensorflow as tf


    device = tf.config.list_physical_devices('GPU')[0]
    tf.config.experimental.set_memory_growth(device, True)


    sent = 'Yes Gladly I am happy with that'
    sentiment_analyser = load_model('../static/sentiment_analyser/model')
    tokenizer = pickle.load(open("../static/tokenizer.pickle", "rb"))
    max_len = 34
    nlp = spacy.load('en_core_web_lg')
    print(is_angry(sent, nlp, sentiment_analyser, tokenizer, max_len))
    


