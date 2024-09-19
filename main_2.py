import json
import os
import random
import time
import re
from dotenv import load_dotenv

from services.TelegramService import TelegramService
from models.Question import Question

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
with open('data/questions.json', encoding="utf8") as f:
    questions = json.load(f)

# Generate a unique seed value based on current time
seed_value = int(time.time())

# Wait some time to generate a new unique seed
time.sleep(2)

# Set the seed value
random.seed(seed_value)

# Get a random question object from the questions.json file
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
    # Get original information before shuffling and trimming
    question_text = random_question["question"][:300]
    options = random_question["options"]
    answer = random_question["answer"]
    explanation = random_question["explanation"][:200]

    question = Question()
    question.id = random_question["id"]
    question.options = options
    question.answer = answer
    question.explanation = explanation
    question.question = question_text


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