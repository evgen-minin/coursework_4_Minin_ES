class Vacancy:
    def __init__(self, job_title: str, url_vacancy: str, salary: str, description: str):
        self.job_title = job_title
        self.url_vacancy = url_vacancy
        self.salary = salary
        self.description = description

    def validate_data(self):
        if not isinstance(self.job_title, str):
            raise TypeError("Название вакансии должно быть строкой")

        if not isinstance(self.url_vacancy, str):
            raise TypeError("Link must be a string.")

        if not isinstance(self.salary, (int, float)) and self.salary is not None:
            raise TypeError("Salary must be a number or None.")

        if not isinstance(self.description, str):
            raise TypeError("Description must be a string.")

        if self.salary is not None and self.salary < 0:
            raise ValueError("Salary must be non-negative or None.")

        if not self.link.startswith('http'):
            raise ValueError("Link must start with http.")

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary
