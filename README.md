# Лабораторная работа №6
Сейчас вы можете видеть очень хорошо выполненный README.md файл, который использует язык разметки [markdown](https://ru.wikipedia.org/wiki/Markdown)
Программа позваляет высчитать оценку исходя из даты сдачи работы, а так же показать, сколько человек просрочили работу.

## Оглавление

1. [Первая функция](#Первая-функция)
2. [Вторая функция](#Вторая-функция)
3. [Вставка изображения](#Вставка-изображения)

## Первая функция
Первая функция *Deadline_score* вычисляет оценку исходя из даты сдачи работы и даты дедлайна. Каждую следующую неделю после дедлайна,
оценка уменьшается на единицу. Минимальная оценка - 0
Код функции:
```python
def deadline_score(pass_date: str, deadline_date: str) -> int:
    """
    Функция сообщает какая будет оценка, исходя из дат дедлайна и сдачи работы
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
```
____
[:arrow_up:Оглавление](#Оглавление)
____
## Вторая функция
Вторая функция *late_list* возвращает список людей, которые сдали работу позже дедлайна. Список людей отсортирован в лексикографическом порядке.
Код функции:
```python
def late_list(grades: dict, deadline_date: str) -> List[str]:
    """
    Функция возвращает список студентов, которые сдали работу после дедлайна
    :param grades: Словарь студентов (студент: дата сдачи работы)
    :param deadline_date: Дата дедлайна
    :return: Список с именами студентов
    """
    deadline_date = dt.date(*map(int, (deadline_date[6:],
                                       deadline_date[3:5], deadline_date[:2])))

    students = []

    for key, value in grades.items():
        value_date = dt.date(*map(int, (value[6:],
                                  value[3:5], value[:2])))

        delta = value_date - deadline_date
        delta = delta.days.real
        if delta > 0:
            students.append(key)

    return sorted(students, key=lambda x: x[0])
```
____
[:arrow_up:Оглавление](#Оглавление)
____
## Вставка изображения
Пример вставки изображения:
![Пример изображения](https://i.ibb.co/2yQKyGf/image.png "Мамин симпотяга")
____
[:arrow_up:Оглавление](#Оглавление)
____