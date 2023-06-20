import json
import os
import random
import requests
import time
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

answer_index = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
}

# Read the environment variables
bot_token = os.getenv('BOT_TOKEN')
target_chat_id = os.getenv('TARGET_CHAT_ID')

if not bot_token or not target_chat_id:
    raise Exception("Please add your environment variables on .env file")

# Read the questions and answers from the JSON file
with open('questions.json') as f:
    questions = json.load(f)

# Generate a unique seed value based on current time
seed_value = int(time.time())

# Wait some time to generate a new unique seed
time.sleep(2)

# Set the seed value
random.seed(seed_value)

# Get a random question object from the questions.json file
random_question = random.choice(questions)


def get_answer_index(letter):
    pattern = r'[:.(),]'
    modified_letter = re.sub(pattern, '', letter)
    return answer_index.get(modified_letter.lower())


def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def send_telegram_message(token, chat_id, text):
    # Set up the URL for the Telegram API
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    # Set up the request payload
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        raise Exception(f'Error sending message: {response.status_code} - {response.text} - {text}')


def send_telegram_poll(token, chat_id):
    # Get original information before shuffling and trimming
    question = random_question["question"][:300]
    options = random_question["options"]
    answer = random_question["answer"]
    explanation = random_question["explanation"][:200]

    # Get the correct option text at the moment based on the original answer
    option_text = options[get_answer_index(answer)][:100]

    # Shuffle the options
    random.shuffle(options)

    # Update answer to the shuffled option index
    # And also trim all the options to 100 characters
    for i in range(len(options)):
        options[i] = options[i][:100]
        if options[i] == option_text:
            answer = find_key_by_value(answer_index, i)

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
        'correct_option_id': get_answer_index(answer),
        'explanation': explanation,
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print('Poll sent successfully!')
    else:
        raise Exception(f'Error sending poll: {response.status_code} - {response.text} - {question}')


def send_photo(token, chat_id, picture_path):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    files = {'photo': open(picture_path, 'rb')}
    params = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=params)

    if response.status_code == 200:
        print('Photo sent successfully!')
    else:
        raise Exception(f'Error sending photo: {response.status_code} - {response.text} - {picture_path}')


# Send all messages if any
if 'messages' in random_question:
    for message in random_question["messages"]:
        send_telegram_message(bot_token, target_chat_id, message)

# Send all photos if any
if 'photos' in random_question:
    for photo in random_question["photos"]:
        send_photo(bot_token, target_chat_id, f"photos/{photo}")

# Send the poll
send_telegram_poll(bot_token, target_chat_id)
