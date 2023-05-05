import json
import random
import requests

# Read the token and chat id from the JSON file
with open('setup.json') as f:
    token = json.load(f)["token"]

with open('setup.json') as f:
    chat_id = json.load(f)["chat_id"]

# Read the questions and answers from the JSON file
with open('questions.json') as f:
    questions = json.load(f)

# Get a random question object from the questions.json file
question_obj = random.choice(questions)

# Get original information before shuffling and trimming
question = question_obj["question"][:300]
options = question_obj["options"]
answer = question_obj["answer"]
explanation = question_obj["explanation"][:200]

# Get the correct option text at the moment based on the original answer
option_text = options[answer][:100]

# Shuffle the options
random.shuffle(options)

# Update answer to the shuffled option index
# And also trim all the options to 100 characters
for i in range(len(options)):
    options[i] = options[i][:100]
    if options[i] == option_text:
        answer = i

# Parse the options into a JSON object
options_json = json.dumps(options)

# Set up the URL for the Telegram API
url = f'https://api.telegram.org/bot{token}/sendPoll'

# Set up the request payload
payload = {
    'chat_id': chat_id,
    'question': question,
    'options': options_json,
    'is_anonymous': True,
    'allows_multiple_answers': False,
    'type': 'quiz',
    'correct_option_id': answer,
    'explanation': explanation,
}

# Send the request to the Telegram API
response = requests.post(url, data=payload)

# Check if the poll was sent successfully
if response.status_code == 200:
    print('Poll sent successfully.')
else:
    raise Exception(f'Error sending poll: {response.status_code} - {response.text} - {question}')