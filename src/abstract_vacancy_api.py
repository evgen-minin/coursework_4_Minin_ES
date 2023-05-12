from abc import ABC, abstractmethod

import requests


class AbstractVacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, vacancy_name: str) -> list[dict]:
        pass

    # @property
    # @abstractmethod
    # def url(self) -> str:
    #     pass

    # @property
    # @abstractmethod
    # def headers(self) -> dict:
    #     pass
