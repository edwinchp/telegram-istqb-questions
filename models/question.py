class Question:
    def __init__(self):
        self.id = None
        self.question = None
        self.messages = []
        self.photos = []
        self.options = []
        self.answer = None
        self.explanation = None
        self.correct_option_id = None

    def serialize(self):
        if isinstance(self, Question):
            return {
                "id": self.id,
                "question": self.question,
                "messages": self.messages,
                "photos": self.photos,
                "options": self.options,
                "answer": self.answer,
                "explanation": self.explanation
            }
        raise TypeError("Object of type {} is not json serializable".format(type(self)))