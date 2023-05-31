import logging
import os
from abc import ABC, abstractmethod
from typing import List
from urllib.error import HTTPError

import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    handlers=[
        logging.FileHandler('vacancy_app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class AbstractVacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, vacancy_name: str) -> list[dict]:
        pass


class MixinAPI:
    """
    Класс миксин, для отправки GET запроса по API.
    """
    url: str = ''
    headers: dict = {}
    params: dict = {}
    field_the_number_of_lines: str = ''
    field_items: str = ''

    def get_vacancies(self, vacancy_name: str) -> List[dict]:
        """
        Отправляет GET-запрос по API и получает список вакансий.
        :param vacancy_name: Название вакансии.
        :return: Список словарей с информацией о вакансиях.
        """
        logger.info("Отправка GET-запроса к API сайтов.")
        list_vacancies: List[dict] = []
        self.params['page'] = 0
        while True:
            try:
                response = requests.get(self.url, headers=self.headers, params=self.params)
                response.raise_for_status()
                vacancy = response.json()
            except requests.exceptions.RequestException as e:
                raise HTTPError(f'Ошибка при отправке запроса: {e}')
            except ValueError as e:
                raise HTTPError(f'Ошибка при обработке ответа: {e}')

            count_vacancy = vacancy[self.field_the_number_of_lines]
            total_pages = (count_vacancy + 99) // 100

            list_vacancies += vacancy[self.field_items]
            self.params['page'] += 1

            if self.params['page'] >= total_pages:
                break

        return list_vacancies


class HeadHunterAPI(MixinAPI, AbstractVacancyAPI):
    """
    Класс для работы с API сайта HeadHunter.
    Наследуется от MixinAPI и AbstractVacancyAPI.
    """
    url: str = 'https://api.hh.ru/vacancies'
    params: dict = {}
    field_the_number_of_lines: str = 'found'
    field_items: str = 'items'
    page: int = 0

    def get_vacancies(self, vacancy_name: str) -> List[dict]:
        self.params = {
            'text': vacancy_name,
            'search_field': 'name',
            'page': self.page,
            'per_page': 100,
        }
        logger.info("Получены вакансии из HeadHunter.")
        return super().get_vacancies(vacancy_name)


class SuperJobAPI(MixinAPI, AbstractVacancyAPI):
    """
    Класс для работы с API сайта SuperJob.
    Наследуется от MixinAPI и AbstractVacancyAPI.
    """
    url: str = 'https://api.superjob.ru/2.33/vacancies/'
    headers: dict = {'X-Api-App-Id': os.getenv('TOKEN_SJOB')}
    params: dict = {}
    page: int = 0
    field_the_number_of_lines: str = 'total'
    field_items: str = 'objects'

    def get_vacancies(self, vacancy_name: str) -> List[dict]:
        self.params = {
            'keywords[0][keys]': vacancy_name,
            'page': self.page,
            'count': 100
        }
        logger.info("Получены вакансии из SuperJob.")
        return super().get_vacancies(vacancy_name)
