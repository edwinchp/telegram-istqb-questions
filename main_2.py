from factories.data_factory import DataFactory
from factories.question_factory import QuestionFactory
from services.TelegramService import TelegramService
from utils.environment_loader import EnvironmentLoader

def main():
    bot_token = EnvironmentLoader.get_bot_token()
    chat_id = EnvironmentLoader.get_chat_id()

    telegram_service = TelegramService(bot_token)

    data = DataFactory.get_random_data()
    question = QuestionFactory.create_question(data)

    if question.messages:
        for message in question.messages:
            telegram_service.send_message(chat_id, message)

    if question.photos:
        for photo in question.photos:
            telegram_service.send_photo(chat_id, photo)

    telegram_service.send_poll(chat_id, question)

if __name__ == '__main__':
    main()