from factories.data_factory import DataFactory
import pytest

@pytest.fixture
def sample_data():
    data = DataFactory.get_all_data()
    return data

class TestData:
    def test_data_has_mandatory_attributes(self, sample_data):
        for data in sample_data:
            assert 'id' in data
            assert 'question' in data
            assert 'options' in data
            assert 'answer' in data
            assert 'explanation' in data