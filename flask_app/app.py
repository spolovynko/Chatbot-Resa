# libraries
import pickle
import json
import spacy
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from nltk.stem import WordNetLemmatizer
from python_scripts.bot_model_prediction import predict_class
from python_scripts.bot_answer import getResponse

lemmatizer = WordNetLemmatizer()

# chat initialization
model = load_model("static/chatbot_model_turing.h5")
intents = json.loads(open("static/intents-venkata.json").read())
words = pickle.load(open("static/words.pkl", "rb"))
classes = pickle.load(open("static/classes.pkl", "rb"))
sentiment_analyser = load_model('static/sentiment_analyser/model')
tokenizer = tokenizer_from_json('static/tokenizer.json')
max_len = 34
nlp = spacy.load('en_core_web_lg')
booking = {'time': '', 'people':'', 'day':''}


app = Flask(__name__)
run_with_ngrok(app) 

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/postUpdate", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    ints = predict_class(msg, model, words, classes, lemmatizer)
    res = getResponse(ints, intents, msg, nlp, sentiment_analyser, tokenizer, max_len, booking)
    return res

if __name__ == "__main__":
    app.run()

