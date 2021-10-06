# ResaBot (Chatbot for booking)
A bot for a large chain of restaurants/hotels. When the customer sends a message on the website of the hotel, the bot should be able to understand the customer's intentions and respond to them. The bot will be partly responsible for its sales department.

## Mission objectives

- Understand and use natural language processing.
- Set up a chatbot using machine learning in a professional context and for commercial purposes.
- Create an API.

### Must-have features

**In English**, the bot should be able to :

- Understand phrases related to a room reservation.
  Example that the bot will have to understand:

  ```text
  > I wish to reserve a room for 2 people.
  > I wish to reserve a room for 4 days
  > Do you have rooms available from July 23rd?
  > I would like to reserve a room for two days and for two people
  ```

- Understand phrases related to a table reservation for the restaurant.

  ```text
  > I would like to make a reservation for tonight.
  > I'd like to reserve a table for four people.
  ```

- Must ensure a continuous and ongoing conversation. Example of a complete conversation :

  ```text
  > Customer : Hello !
  > Bot : Hello, how can I help you?
  > Customer: I would like to reserve a table for 4 people ?
  > Bot : For which date would you like to reserve your table?
  > Customer : Today at 7:00 pm
  > Bot : What name should I make the reservation under?
  > Customer  : My name is Mr. Dupont!
  > Bot : Very well Mr Dupont, I confirm you the reservation of a table for 4 people tonight at 7:00 pm.
  > Bot : Can I help you with something else?
  > Customer : No thanks
  > Bot: Have a nice day.
  ```

- Understand when the client is angry. In this case, the bot will indicate that it is transmitting the conversation to a human.

  ```text
  > You're incompetent!
  > My room is dirty! This is outrageous!
  > I want to talk to a human.
  ```
# Process:

As part of the project we have decdided to build two models one is for Text Analysis and the second is for the Sentiment Analysis to know about the feeling of the customer as part of converation through the Bot.


# What did we do?

 - API has been developed using Flask  
 - Model for Text Analysis has been developed and Integrated with flask app
 - Model for Sentiment Analysis has been developed but not yet fully Integrated with Flask app.

# Technologies used
 -Python 3.9
 -Tensorflow
 -nltk,spacy 
 -Flask
 -Jupyter Notebook
 -Pycharm
  







