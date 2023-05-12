from abc import ABC, abstractmethod


class AbstractVacancyData(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
