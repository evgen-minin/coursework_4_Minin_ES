from typing import List


class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, id: str, url: str, title: str, salary: float, description: str, company_name: str):
        self.id = id
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description
        self.company_name = company_name
        self.validate()

    def to_dict(self) -> dict:
        """
        Преобразует данные в словарь.
        :return: Возвращает данные в виде словаря.
        """
        return {
            'id вакансии': self.id,
            'Название вакансии': self.title,
            'Ссылка на вакансию': self.url,
            'Зарплата': self.salary,
            'Описание вакансии': self.description,
            'Название организации': self.company_name
        }

    def validate(self) -> None:
        """
        Проверяет атрибуты объекта Vacancy.
        """
        if self.title is None or not isinstance(self.title, str):
            raise TypeError("Некорректный тип данных для атрибута 'title'")
        if self.url is None or not isinstance(self.url, str):
            raise TypeError("Некорректный тип данных для атрибута 'url'")
        if self.description is None:
            self.description = 'Отсутствует описание'
        elif not isinstance(self.description, str):
            raise TypeError("Некорректный тип данных для атрибута 'description'")
        if self.salary is None:
            self.salary = 'Зарплата не указана'
        elif not isinstance(self.salary, (float, int)):
            raise TypeError("Некорректный тип данных для атрибута 'salary'")

    def __repr__(self) -> str:
        return f"Vacancy(title='{self.title}', url='{self.url}', salary={self.salary}, description='{self.description}')"

    def __eq__(self, other) -> bool:
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        raise TypeError("Невозможно сравнить объекты других типов")

    def get_sorted_by_salary(self) -> List[dict]:
        """
        Сортирует данные по зарплате.
        """""
        sorted_vacancies = sorted(self.vacancies, key=lambda vacancy: vacancy.get('Зарплата'))
        return sorted_vacancies
