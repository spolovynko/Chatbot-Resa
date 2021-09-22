import random
from flask_app.python_scripts.user_input_analysis import is_angry

def getResponse(ints, intents_json, msg, nlp, sentiment_analyser, tokenizer, max_len, status):
    tag = ints[0]["intent"]
    if tag== 'noanswer':
        return no_answer(msg, nlp, sentiment_analyser, tokenizer, max_len, status)   
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            return random.choice(i["responses"])


def no_answer(msg, nlp, sentiment_analyser, tokenizer, max_len, status):
    angry = is_angry(msg, nlp, sentiment_analyser, tokenizer, max_len)
    if angry:
        status[2] = True
        return 'Would you like to talk to one of our collaborator to get more information?'
    else:
        return fill_booking(status)


def fill_booking(status):
    if not status['booking']['day']:
        status['info_required'] = 'day'
        return 'Which day would you like to book a table?'
    elif not status['booking']['time']:
        status['info_required'] = 'day'
        return 'At which time would you like to come?'
    else:
        status['info_required'] = 'people'
        return 'How many people will be there?'




def extract_info(sentence, nlp):
    sent = nlp(sentence)
    
        