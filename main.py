from utils import load_students, load_professions, get_profession_by_title, \
    get_student_by_pk, check_fitness, show_result


def main():
    """
    Здесь собрана логика программы

    :return: None
    """
    student = load_students('https://jsonkeeper.com/b/WIVC')
    profession = load_professions('https://jsonkeeper.com/b/SA1G')

    user = int(input('Введите номер студента: '))
    student_result = get_student_by_pk(student, user)
    if not student_result:
        quit('У нас нет такого студента')

    user = input(f'Выберите специальность для оценки студента '
                 f'>: {student_result["full_name"]} :<\n>: ')
    profession_result = get_profession_by_title(profession, user)
    if not profession_result:
        quit('У нас нет такой специальности')

    check = check_fitness(student_result, profession_result)
    print(show_result(check, student_result))


if __name__ == '__main__':
    main()
