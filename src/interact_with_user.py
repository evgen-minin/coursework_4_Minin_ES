from src.saving_information_vacancies import JSONVacancyStorage
from src.vacancies import Vacancy
from src.vacancies_search_api import SuperJobAPI, HeadHunterAPI
import re


def interact_with_user():
    """
    Функция для взаимодействия с пользователем.
    """
    print("Добро пожаловать в программу по поиску вакансий!")

    while True:
        print("Выберите платформу:\n1. HeadHunter\n2. SuperJob")
        platform_choice = input("Введите номер платформы: ")

        if platform_choice.isdigit():  # Проверяем, является ли ввод числом
            platform_choice = int(platform_choice)

            if platform_choice == 1:
                hh_api = HeadHunterAPI()
                vacancy_name = input("Введите название вакансии: ")

                if not re.match(r'^[a-zA-Zа-яА-Я]+$', vacancy_name.strip()):
                    print("Название вакансии должно содержать только буквы. Попробуйте снова.")
                    continue

                vacancies = hh_api.get_vacancies(vacancy_name)
                storage = JSONVacancyStorage()

                for vacancy in vacancies:
                    salary = vacancy['salary']['from'] if vacancy['salary'] and 'from' in vacancy['salary'] else None
                    job_vacancy = Vacancy(
                        id=vacancy['id'],
                        title=vacancy['name'],
                        url=vacancy['alternate_url'],
                        salary=salary,
                        description=vacancy['snippet']['responsibility'],
                        company_name=vacancy['employer']['name']
                    )
                    storage.add_vacancy(job_vacancy.to_dict())
                storage.save_to_json('files_with_vacancies/hh_vacancies.json')

            elif platform_choice == 2:
                superjob_api = SuperJobAPI()
                vacancy_name = input("Введите название вакансии: ")

                if not re.match(r'^[a-zA-Zа-яА-Я]+$', vacancy_name.strip()):
                    print("Название вакансии должно содержать только буквы. Попробуйте снова.")
                    continue

                vacancies = superjob_api.get_vacancies(vacancy_name)
                storage = JSONVacancyStorage()

                for vacancy in vacancies:
                    salary = vacancy['payment_from'] if vacancy['payment_from'] else None
                    job_vacancy = Vacancy(
                        id=vacancy['id'],
                        title=vacancy['profession'],
                        url=vacancy['link'],
                        salary=salary,
                        description=vacancy['candidat'],
                        company_name=vacancy['firm_name']
                    )
                    storage.add_vacancy(job_vacancy.to_dict())
                storage.save_to_json('files_with_vacancies/super_job_vacancies.json')

            else:
                print("Неверно указан номер платформы. Попробуйте снова.")
                continue

            print("Данные о вакансиях сохранены в файл")

            choice = input("Хотите вывести вакансии, отсортированные по зарплате? (да/нет): ")

            if choice.lower() == "да":
                sorted_vacancies = sorted(
                    (v for v in storage.vacancies if
                     v.get('Зарплата') is not None and isinstance(v.get('Зарплата'), (int, float))),
                    key=lambda v: float(v['Зарплата']),
                    reverse=True
                )

                top_vacancies = sorted_vacancies[:10]

                print("\nТоп 10 вакансий с самыми большими зарплатами:")

                for vacancy in top_vacancies:
                    title = vacancy.get('Название вакансии', 'Название не указано')
                    salary = vacancy.get('Зарплата', 'Зарплата не указана')
                    description = vacancy.get('Описание вакансии', 'Описание не указано')
                    url = vacancy.get('Ссылка на вакансию', 'Ссылка не указана')
                    company_name = vacancy.get('Название организации', 'Компания не указана')

                    print(f"Название: {title}")
                    print(f"Зарплата: {salary}")
                    print(f"Описание: {description}")
                    print(f"Ссылка: {url}")
                    print(f"Компания: {company_name}")

            elif choice.lower() == "нет":
                pass

            else:
                print("Некорректный ввод. Попробуйте снова.")
                continue

            break

        else:
            print("Неверный формат ввода. Пожалуйста, введите число.")
