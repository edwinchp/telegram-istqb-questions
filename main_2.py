import json
import os
import random
import time
import re
from dotenv import load_dotenv

from factories.data_factory import DataFactory
from factories.question_factory import QuestionFactory
from services.TelegramService import TelegramService
from models.question import Question

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('TARGET_CHAT_ID')

# All answers supported
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

if not BOT_TOKEN or not CHAT_ID:
    raise Exception("Please add your environment variables on .env file")

# Read the questions and answers from the JSON file
with open('data/data.json', encoding="utf8") as f:
    questions = json.load(f)

# Generate a unique seed value based on current time
seed_value = int(time.time())

# Wait some time to generate a new unique seed
time.sleep(2)

# Set the seed value
random.seed(seed_value)

# Get a random question object from the data.json file
random_question = random.choice(questions)


# Get index based on letter which is formatted
def get_answer_index(letter):
    pattern = r'[:.(),]'
    modified_letter = re.sub(pattern, '', letter)
    return answer_index.get(modified_letter.lower())


# Get the letter based on the index
def find_key_by_value(dictionary, index):
    for key, val in dictionary.items():
        if val == index:
            return key
    return None


def main():
    telegram_service = TelegramService(BOT_TOKEN)

    data = DataFactory.get_data_by_position(0)
    question = QuestionFactory.create_question(data)

    telegram_service.send_poll(CHAT_ID, question)

    # Send all messages if any
    if 'messages' in random_question:
        for message in random_question["messages"]:
            telegram_service.send_message(CHAT_ID, random_question)

    # Send all photos if any
    if 'photos' in random_question:
        for photo in random_question["photos"]:
            telegram_service.send_photo(BOT_TOKEN, random_question)

if __name__ == '__main__':
    main()