from factories.data_factory import DataFactory
from factories.question_factory import QuestionFactory
import pytest


@pytest.fixture
def sample_question():
    data = DataFactory.get_random_data()
    question = QuestionFactory.create_question(data)
    return question

class TestQuestion:
    def test_question_has_id(self, sample_question):
        assert sample_question is not None