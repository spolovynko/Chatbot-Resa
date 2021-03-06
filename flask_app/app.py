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
tokenizer = pickle.load(open("static/tokenizer.pickle", "rb"))
max_len = 34
nlp = spacy.load('en_core_web_sm')
booking = {'time': '', 'people':'', 'day':''}
status = {'booking': booking, 'info_required': None, 'booking_started': False, 'angry': False, 'booking_compelete': False}

app = Flask(__name__)
# run_with_ngrok(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/postUpdate", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    ints = predict_class(msg, model, words, classes, lemmatizer)
    res = getResponse(ints, intents, msg, nlp, sentiment_analyser, tokenizer, max_len, status)
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

