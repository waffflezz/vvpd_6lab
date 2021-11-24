"""
Скоробогатов Дмитрий Алексеевич, 15 вариант (2 задание), КИ21-17/1б
"""


import re
import datetime as dt
import math


def main():
    months = {
        '01': '31', '02': '28', '03': '31', '04': '30',
        '05': '31', '06': '30', '07': '31', '08': '31',
        '09': '30', '10': '31', '11': '30', '12': '31',
    }
    dates_list = []

    print('Введите сначала дату сдачи лабораторной, а затем дату дедлайна')
    while len(dates_list) != 2:
        n = input()

        if not re.fullmatch(r'\d\d\.\d\d\.\d{4}', n):
            raise ValueError
        if n[3:5] not in months or int(n[:2]) > int(months[n[3:5]]):
            raise ValueError
        
        dates_list.append(n)

    print(f'Оценка = {5 - deadline_score(dates_list[0], dates_list[1])}')


def deadline_score(pass_date: str, deadline_date: str) -> int:
    """
    Функция сообщает какая будет оценка, исходя из даты дедлайна и
    даты сдачи работы
    :param pass_date: Дата сдачи
    :param deadline_date: Дата дедлайна
    :return: Оценка
    """
    pass_date = dt.date(*map(int, (pass_date[6:],
                                   pass_date[3:5], pass_date[:2])))

    deadline_date = dt.date(*map(int, (deadline_date[6:],
                                 deadline_date[3:5], deadline_date[:2])))

    delta = pass_date - deadline_date
    delta = delta.days.real
    if delta < 0:
        return 0

    bad_rating = math.ceil(delta / 7)

    if bad_rating > 5:
        return 5

    return bad_rating


if __name__ == '__main__':
    main()
