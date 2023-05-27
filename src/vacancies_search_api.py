import os

import requests

from exept import HTTPError
from src.abstract_vacancy_api import AbstractVacancyAPI


class MixinAPI:
    url = ''
    headers = {}
    params = {}
    field_the_number_of_lines = ''
    field_items = ''

    def get_vacancies(self, vacancy_name):
        list_vacancies = []
        start = True
        while start:
            try:
                response = requests.get(self.url, headers=self.headers,
                                        params=self.params)
                response.raise_for_status()
                vacancy = response.json
            except requests.exceptions.RequestException as e:
                raise HTTPError(f'Ошибка при отправке запроса: {e}')
            except ValueError as e:
                raise HTTPError(f'Ошибка при обработке ответа: {e}')
            count_vacancy = vacancy[self.field_the_number_of_lines]
            total_pages = (count_vacancy + 99) // 100

            list_vacancies += vacancy[self.field_items]
            start = self.params['page'] != total_pages
            self.params['page'] += 1
        return list_vacancies


class HeadHunterAPI(MixinAPI, AbstractVacancyAPI):
    url = 'https://api.hh.ru/vacancies'
    params = {}
    page = 0
    field_the_number_of_lines = 'found'
    field_items = 'items'

    def get_vacancies(self, vacancy_name):
        self.params = {
            'text': vacancy_name,
            'search_field': 'name',
            'per_page': 100,
            'page': self.page
        }
        return super().get_vacancies(vacancy_name)


class SuperJobAPI(MixinAPI, AbstractVacancyAPI):
    url = 'https://api.superjob.ru/2.33/vacancies/'
    headers = {'X-Api-App-Id': os.getenv('TOKEN_SJOB')}
    params = {}
    page = 0
    field_the_number_of_lines = 'total'
    field_items = 'objects'

    def get_vacancies(self, vacancy_name):
        self.params = {
            'keywords[0][keys]': vacancy_name,
            'keywords[0][srws]': 1,
            'page': self.page, 'count': 100
        }
        return super().get_vacancies(vacancy_name)
