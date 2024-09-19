import json

class JsonReader:

    @staticmethod
    def get_results(path):
        with open(path, encoding="utf8") as f:
            return json.load(f)