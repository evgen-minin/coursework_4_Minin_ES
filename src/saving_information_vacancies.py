import json
from abc import ABC, abstractmethod
from typing import List


class AbstractVacancyStorage(ABC):
    """
    Абстрактный класс для работы с данными о вакансиях.
    """

    @abstractmethod
    def add_vacancy(self, vacancy: dict) -> None:
        """
        Добавляет информацию о вакансии в файл.
        :param vacancy: Словарь с данными о вакансии.
        :return: None.
        """
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict) -> List[dict]:
        """
        Возвращает список вакансий, удовлетворяющих указанным критериям.
        :param criteria:  Словарь с критериями для фильтрации вакансий.
        :return: Список словарей с данными о вакансиях.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: str) -> None:
        """
        Удаляет информацию о вакансии по её идентификатору.
        :param vacancy_id: Идентификатор вакансии.
        :return: None.
        """
        pass


class JSONVacancyStorage(AbstractVacancyStorage):
    """
    Класс для добавления, сохранения и удаления вакансий.
    """
    def __init__(self):
        self.vacancies = []

    def add_vacancy(self, vacancy_data: dict) -> None:
        """
        Добавляет вакансии
        """
        self.vacancies.append(vacancy_data)

    def get_vacancies(self, criteria: dict) -> List[dict]:
        """
        Возвращает список вакансий по указанным критериям.
        """
        result = []
        for vacancy in self.vacancies:
            if all(vacancy.get(key) == value for key, value in criteria.items()):
                result.append(vacancy)
        return result

    def delete_vacancy(self, vacancy_id: str) -> None:
        """
        Удаляет вакансию по ID.
        """
        for vacancy in self.vacancies:
            if vacancy['id'] == vacancy_id:
                self.vacancies.remove(vacancy)
                break

    def save_to_json(self, filename: str) -> None:
        """
        Сохраняет данные о вакансиях в JSON файл.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)
