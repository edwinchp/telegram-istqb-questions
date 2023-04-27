import telegram
import json
import random
import time
import requests

from telegram.ext import Updater

# Read the token and chat id from the JSON file
with open('setup.json') as f:
    token = json.load(f)["token"]

with open('setup.json') as f:
    chat_id = json.load(f)["chat_id"]

# Read the questions and answers from the JSON file
with open('questions.json') as f:
    questions = json.load(f)


# Replace YOUR_QUESTION with the question you want to ask in the poll
question_obj = random.choice(questions)

# Replace YOUR_OPTIONS with a list of up to 10 options for the poll
options = question_obj["options"]
answer = question_obj["answer"]
print("answer: " + str(answer))

correct_option = options[answer]
print("correct option: " + correct_option)

random.shuffle(options)

for index, option in enumerate(options):
    print(str(index) + ": " + option)
    if option == correct_option:
        answer = index

print("answer: " + str(answer))
correct_option = options[answer]
print("correct option: " + correct_option)


options_json = json.dumps(options)

# Set up the URL for the Telegram API
url = f'https://api.telegram.org/bot{token}/sendPoll'

# Set up the request payload
payload = {
    'chat_id': chat_id,
    'question': question_obj["question"],
    'options': options_json,
    'is_anonymous': True,
    'allows_multiple_answers': False,
    'type': 'quiz',
    'correct_option_id': answer
}

# Send the request to the Telegram API
response = requests.post(url, data=payload)

# Check if the poll was sent successfully
if response.status_code == 200:
    print('Poll sent successfully.')
else:
    print(f'Error sending poll: {response.status_code} - {response.text}')