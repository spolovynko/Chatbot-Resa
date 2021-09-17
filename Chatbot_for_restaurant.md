# ResaBot (Chatbot for booking)

- Repository: `resabot`
- Type of Challenge: Consolidation
- Duration: 5 days
- Deadline: `dd/mm/yy H:i AM/PM`
- Deployment strategy :
  - selfhosting
- Team challenge : `(max 3)`
- Prerequisite :
  - Python Advanced
  - Docker
  - Basic knowledge of NLP and classification

## Mission objectives

- Understand and use natural language processing.
- Set up a chatbot using machine learning in a professional context and for commercial purposes.
- Create an API.

## The Mission

Your mission will be to create ResaBot, a bot for a large chain of restaurants/hotels. When the customer sends a message on the Facebook page of the hotel, the bot should be able to understand the customer's intentions and respond to them. The bot will be partly responsible for its sales department.

To do so, you will have to use neural networks and especially transformers.

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

### Nice-to-have features

- Create an API of your bot to make it cross-platform.
- Use Docker.

## Deliverables

1. Publish your source code on the GitHub repository.
2. Pimp up the README file:

   - Description
   - Installation
   - Usage
   - (Visuals)
   - (Contributors)
   - (Timeline)
   - (Personal situation)
   - It must contain a link to the "live" version.

3. Publish the link to the "live" version on your startup's Discord channel and on your GitHub. The "live" version must contain a link to the source code on GitHub.

### Steps

1. Create the repository.
2. Study the request (What & Why ?)
3. Identify technical challenges (How ?)
4. Find and preprocess a dataset.
5. Train your model and improve your dataset for better results.

## Evaluation criteria

1. You use Git from the start and during the entire process of the development (at least one push per day).
1. The bot must be able to respond to the same sentence but asked differently.
1. The bot must be able to have an ongoing conversation.
1. The bot has to recognize when the customer is unhappy.

> One day we will dominate humans
> -An anonymous bot

![robots](https://media.giphy.com/media/iFCQhoTjoOgms/source.gif)
