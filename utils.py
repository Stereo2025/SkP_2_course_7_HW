import requests
import json


def load_students(source_url: str) -> list:
    """
    Распаковывает json список по http ссылке

    :param source_url: принимает URL ссылку
    :return: list
    """
    resp = requests.get(source_url)
    students = resp.json()
    return students


def load_professions(source_url: str) -> list:
    """
    Распаковывает json список по http ссылке

    :param source_url: принимает URL ссылку
    :return: list
    """
    resp = requests.get(source_url)
    professions = resp.json()
    return professions


def get_student_by_pk(student: list, user: int) -> dict:
    """
    Записывает в словарь данные о студенте, если такой имеется по ключу "pk"

    :param user: Выбор номера студента.
    :param student: Загруженный по ссылке и обработанный список "лист" студентов и скилов.
    :return: Записанные словарь, либо выводится сообщение об "ошибке" и выход из программы.
    """

    for line in student:
        if user == line["pk"]:
            dict_result = {"pk": line["pk"],
                           "full_name": line["full_name"],
                           "skills": line["skills"]}
            return dict_result


def get_profession_by_title(profession: list, user: str) -> dict:
    """
    Записывает в словарь данные по пользовательскому вводу для дальнейшей обработки.

    :param user: Выбор направления.
    :param profession: Загруженный по ссылке и обработанный список "лист" профессий и скилов.
    :return: Записанные словарь, либо выводится сообщение об "ошибке" и выход из программы.
    """

    for line in profession:
        if user.lower() == line["title"].lower():
            dict_result = {"skills": line["skills"]}
            return dict_result


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Проверяет пересечения, а так же разность между навыками студента и необходимыми,
    вычисляет % пригодности.

    :param student: Выбираем из функции load_students ключ "skills".
    :param profession: Выбираем из функции load_professions ключ "skills".
    :return: Словарь с сформированными данными по пользовательскому вводу.
    """

    skills = set(student["skills"]).intersection(set(profession["skills"]))
    no_skills = set(profession["skills"]).difference(set(student["skills"]))
    percent = round(len(skills) / len(set(profession["skills"])) * 100)

    dict_result = {"has": skills,
                   "lacks": no_skills,
                   "fit_percent": percent}

    return dict_result


def show_result(check: dict, student_result: dict) -> str:
    """
    Показывает результат работы программы.

    :param check: Результат работы функции check_fitness.
    :param student_result: Из функции get_student_by_pk берем имя по ключу.
    :return: Строковые значения, результат работы функции.
    """

    return f'\nСтудент: {student_result["full_name"]}\n' \
           f'Знает: {", ".join(check["has"])}\nНе знает: {", ".join(check["lacks"])}\n' \
           f'Пригодность: {check["fit_percent"]} %'
