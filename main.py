from exept import HTTPError
from src.vacancies_search_api import HeadHunterAPI


def main():
    hh_api = HeadHunterAPI()
    try:
        hh_vacancies = hh_api.get_vacancies("Python")
    except HTTPError as e:
        print(e.message)
    print()
    # superjob_api = SuperJobAPI()
    # superjob_vacancies = superjob_api.get_vacancies("Python")
    # print(superjob_vacancies)


if __name__ == "__main__":
    main()