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
question = 'What is your favorite color?'

# Replace YOUR_OPTIONS with a list of up to 10 options for the poll
options = ['Option 1', 'Option 2', 'Option 3']
options_json = json.dumps(options)

# Set up the URL for the Telegram API
url = f'https://api.telegram.org/bot{token}/sendPoll'

# Set up the request payload
payload = {
    'chat_id': chat_id,
    'question': question,
    'options': options_json,
    'is_anonymous': False,
    'allows_multiple_answers': False,
    'type': 'quiz',
    'correct_option_id': 0
}

# Send the request to the Telegram API
response = requests.post(url, data=payload)

# Check if the poll was sent successfully
if response.status_code == 200:
    print('Poll sent successfully.')
else:
    print(f'Error sending poll: {response.status_code} - {response.text}')