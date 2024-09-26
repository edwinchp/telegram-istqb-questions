import json

import requests

class TelegramService:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_poll(self, chat_id, question):
        url = f'https://api.telegram.org/bot{self.bot_token}/sendPoll'

        payload = {
            'chat_id': chat_id,
            'question': question.question,
            'options': json.dumps(question.options),
            'is_anonymous': True,
            'allows_multiple_answers': False,
            'type': 'quiz',
            'correct_option_id': question.correct_option_id,
            'explanation': question.explanation,
        }

        response = requests.post(url, data = payload)

        if response.status_code != 200:
            raise Exception(f'Error sending poll: {response.status_code} - {response.text} - {question}')

        return response

    def send_message(self, chat_id, text):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, json=payload)

        if response.status_code != 200:
            raise Exception(f'Error sending message: {response.status_code} - {response.text} - {text}')

        return response

    def send_photo(self, chat_id, photo_path):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendPhoto"

        files = {'photo': open('photos/' + photo_path, 'rb')}
        payload = {'chat_id': chat_id}
        response = requests.post(url, files=files, data=payload)

        if response.status_code != 200:
            raise Exception(f'Error sending photo: {response.status_code} - {response.text} - {photo_path}')

        return response
