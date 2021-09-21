import json


def booking():
    verbs = ['want', 'would like', 'wish']
    complements = ['to book a table', 'a table']
    times = ['this morning', 'for lunch', 'for this evening', 'for tomorow evening']

    bookings = [f"I {verb} {complement} {time}" for verb in verbs for time in times for complement in complements]
    return bookings

def payments():
    questions = ['Do you', 'are you']
    verbs = ['take', 'taking', 'accept']
    cards = ['Credit cards', 'master cards', 'cards', 'cash']

    payment = [f'{question} {verb} {card}?' for question in questions for verb in verbs for card in cards]
    payment.append('Are cash only.')
    return payment

def greetings():
    sentences = []


def json_build():
    tags = ['booking', 'payments']
    intents = [booking, payments]
    data = {tag: intent() for tag, intent in zip(tags, intents)}
    with open('restaurant.json', 'w') as f:
        json.dump(data, f)

if __name__=='__main__':
    json_build()


