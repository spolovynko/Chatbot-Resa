import random
from python_scripts.user_input_analysis import is_angry

def getResponse(ints, intents_json, msg, nlp, model, tokenizer, max_len, booking):
    tag = ints[0]["intent"]
    if tag== 'noanswer':
        angry = is_angry(msg, nlp, model, tokenizer, max_len)
        if angry:
            return 'Please, wait a moment. One of our collaborator will contact you to provide you more efficient service.'
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result