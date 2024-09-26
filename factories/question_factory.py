import json
import random
import re

from models.question import Question

class QuestionFactory:

    SUPPORTED_ANSWERS = {
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

    @staticmethod
    def create_question(data):
        correct_answer_before_shuffle = data['options'][QuestionFactory.get_answer_index(data['answer'])][:100]
        question = Question()
        question.id = data["id"]
        question.options = QuestionFactory.shuffle_options(data['options'])
        question.answer = QuestionFactory.get_correct_answer(question.options, correct_answer_before_shuffle)
        question.correct_option_id = QuestionFactory.get_answer_index(question.answer)
        question.explanation = data["explanation"]
        question.question = data["question"]
        return question

    @staticmethod
    def get_answer_index(letter):
        pattern = r'[:.(),]'
        modified_letter = re.sub(pattern, '', letter)
        return QuestionFactory.SUPPORTED_ANSWERS.get(modified_letter.lower())

    @staticmethod
    def shuffle_options(options):
        random.shuffle(options)
        return options

    @staticmethod
    def get_correct_answer(options, answer):
        for i in range(len(options)):
            options[i] = options[i][:100]
            if options[i] == answer:
                answer = QuestionFactory.find_key_by_value(QuestionFactory.SUPPORTED_ANSWERS, i)
        return answer

    @staticmethod
    def find_key_by_value(dictionary, index):
        for key, val in dictionary.items():
            if val == index:
                return key
        return None