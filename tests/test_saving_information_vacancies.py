import json
import pytest
from tempfile import NamedTemporaryFile

from src.saving_information_vacancies import JSONVacancyStorage


@pytest.fixture
def storage():
    return JSONVacancyStorage()


@pytest.fixture
def sample_vacancy_data():
    return {
        'id': '12345',
        'url': 'https://example.com',
        'title': 'Software Engineer',
        'salary': 5000.0,
        'description': 'Lorem ipsum dolor sit amet.',
        'company_name': 'Example Company'
    }


def test_add_vacancy(storage, sample_vacancy_data):
    storage.add_vacancy(sample_vacancy_data)
    assert len(storage.vacancies) == 1
    assert storage.vacancies[0] == sample_vacancy_data


def test_get_vacancies(storage, sample_vacancy_data):
    storage.add_vacancy(sample_vacancy_data)
    criteria = {'title': 'Software Engineer'}
    result = storage.get_vacancies(criteria)
    assert len(result) == 1
    assert result[0] == sample_vacancy_data


def test_get_vacancies_no_match(storage, sample_vacancy_data):
    storage.add_vacancy(sample_vacancy_data)
    criteria = {'title': 'Data Scientist'}
    result = storage.get_vacancies(criteria)
    assert len(result) == 0


def test_delete_vacancy(storage, sample_vacancy_data):
    storage.add_vacancy(sample_vacancy_data)
    assert len(storage.vacancies) == 1
    vacancy_id = sample_vacancy_data['id']
    storage.delete_vacancy(vacancy_id)
    assert len(storage.vacancies) == 0


def test_save_to_json(storage, sample_vacancy_data):
    storage.add_vacancy(sample_vacancy_data)
    with NamedTemporaryFile() as tmp_file:
        storage.save_to_json(tmp_file.name)
        with open(tmp_file.name, 'r') as file:
            data = json.load(file)
        assert len(data) == 1
        assert data[0] == sample_vacancy_data
