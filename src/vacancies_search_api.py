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
        page = 0
        start = True
        while start:
            try:
                vacancy = requests.get(self.url, headers=self.headers,
                                   params=self.params).json()
                test = 1/0
            except ZeroDivisionError as e:
                raise HTTPError(f'ыпывпывп: {e}')
            pages = vacancy[self.field_the_number_of_lines]
            list_vacancies += vacancy[self.field_items]
            start = page != pages
            page += 1
        return list_vacancies


class HeadHunterAPI(MixinAPI, AbstractVacancyAPI):
    url = 'https://api.hh.ru/vacancies'
    params = {}
    page = 0
    field_the_number_of_lines = 'pages'
    field_items = 'items'

    def get_vacancies(self, vacancy_name):
        self.params = {'text': vacancy_name, 'search_field': 'name', 'per_page': 100,
                       'page': self.page}
        return super().get_vacancies(vacancy_name)

    class SuperJobAPI(AbstractVacancyAPI):
        url = 'https://api.superjob.ru/2.33/vacancies/'

        # @property
        # def url(self) -> str:
        #     return 'https://api.superjob.ru/2.33/vacancies/'

        # @property
        # def headers(self) -> dict:
        #     app_id: str = os.getenv('TOKEN_SJOB')
        #     return {'X-Api-App-Id': app_id}

        def get_vacancies(self, vacancy_name):
            req = requests.get(self.url, headers=self.headers, params={'keyword': vacancy_name})
            return req.json()
