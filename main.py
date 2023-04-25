import telegram
import json
import random
import time

# Read the token and chat id from the JSON file
with open('setup.json') as f:
    bot = json.load(f)["token"]

with open('setup.json') as f:
    chat_id = json.load(f)["chat_id"]

# Read the questions and answers from the JSON file
with open('questions.json') as f:
    questions = json.load(f)


while True:
    # Choose a random question from the list
    question = random.choice(questions)

    # Re-order the options randomly
    random.shuffle(question['options'])

    # Send the poll to the Telegram chat
    poll = bot.send_poll(chat_id=chat_id, question=question['question'], options=question['options'], correct_option_id=question['answer'])

    # Wait for 60 seconds before sending the next poll
    time.sleep(60)