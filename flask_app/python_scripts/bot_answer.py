import random
from flask_app.python_scripts.user_input_analysis import is_angry

def getResponse(ints, intents_json, msg, nlp, sentiment_analyser, tokenizer, max_len, status):
    tag = ints[0]["intent"]
    if tag== 'noanswer':
        angry = is_angry(msg, nlp, sentiment_analyser, tokenizer, max_len)
        if angry:
            status[2] = True
            return 'Would you like to talk to one of our collaborator to get more information?'
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result