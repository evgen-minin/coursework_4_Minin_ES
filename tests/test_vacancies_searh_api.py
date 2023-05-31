import pytest

from src.vacancies_search_api import HeadHunterAPI, SuperJobAPI


@pytest.fixture
def headhunter_api():
    return HeadHunterAPI()


@pytest.fixture
def superjob_api():
    return SuperJobAPI()


def test_headhunter_api_get_vacancies(headhunter_api):
    vacancy_name = "Python Developer"
    vacancies = headhunter_api.get_vacancies(vacancy_name)
    assert isinstance(vacancies, list)
    assert len(vacancies) > 0
    for vacancy in vacancies:
        assert "name" in vacancy
        assert "id" in vacancy


def test_superjob_api_get_vacancies(superjob_api):
    vacancy_name = "Data Scientist"
    vacancies = superjob_api.get_vacancies(vacancy_name)
    assert isinstance(vacancies, list)
    assert len(vacancies) > 0
    for vacancy in vacancies:
        assert "profession" in vacancy
        assert "id" in vacancy
