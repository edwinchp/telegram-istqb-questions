import random
import time

from utils.json_reader import JsonReader


class DataFactory:

    @staticmethod
    def get_random_data():
        data = JsonReader.get_results('data/data.json')
        seed_value = int(time.time())
        random.seed(seed_value)
        return random.choice(data)

    @staticmethod
    def get_data_by_position(position):
        data = JsonReader.get_results('data/data.json')
        return data[position]

    @staticmethod
    def get_all_data():
        data = JsonReader.get_results('data/data.json')
        return data