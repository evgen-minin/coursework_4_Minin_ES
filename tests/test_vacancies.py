import pytest

from src.vacancies import Vacancy


@pytest.fixture
def valid_vacancy_data():
    return {
        'id': '12345',
        'url': 'https://example.com',
        'title': 'Software Engineer',
        'salary': 5000.0,
        'description': 'Lorem ipsum dolor sit amet.',
        'company_name': 'Example Company'
    }


def test_vacancy_init_invalid_title_type(valid_vacancy_data):
    valid_vacancy_data['title'] = 12345
    with pytest.raises(TypeError):
        Vacancy(**valid_vacancy_data)


def test_vacancy_init_invalid_url_type(valid_vacancy_data):
    valid_vacancy_data['url'] = 12345
    with pytest.raises(TypeError):
        Vacancy(**valid_vacancy_data)


def test_vacancy_init_invalid_description_type(valid_vacancy_data):
    valid_vacancy_data['description'] = 12345
    with pytest.raises(TypeError):
        Vacancy(**valid_vacancy_data)


def test_vacancy_init_invalid_salary_type(valid_vacancy_data):
    valid_vacancy_data['salary'] = '5000.0'
    with pytest.raises(TypeError):
        Vacancy(**valid_vacancy_data)


def test_vacancy_eq_operator(valid_vacancy_data):
    vacancy1 = Vacancy(**valid_vacancy_data)
    vacancy2 = Vacancy(**valid_vacancy_data)
    assert vacancy1 == vacancy2
