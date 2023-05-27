from abc import ABC, abstractmethod


class AbstractVacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, vacancy_name: str) -> list[dict]:
        pass
