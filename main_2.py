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

if not BOT_TOKEN or not CHAT_ID:
    raise Exception("Please add your environment variables on .env file")

def main():
    telegram_service = TelegramService(BOT_TOKEN)

    data = DataFactory.get_data_by_position(5)
    question = QuestionFactory.create_question(data)



    # Send all messages if any
    if question.messages:
        for message in question.messages:
            telegram_service.send_message(CHAT_ID, message)

    # Send all photos if any
    if question.photos:
        for photo in question.photos:
            telegram_service.send_photo(BOT_TOKEN, photo)

    telegram_service.send_poll(CHAT_ID, question)

if __name__ == '__main__':
    main()