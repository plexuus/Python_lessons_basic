try:
    from .functions import *
except ImportError:
    from lesson01.home_work.functions import *

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

def task1():
    def list_sqrt(temp_list):
        if not isinstance(temp_list, list):
            return False

        import math

        out_list = list()
        for item in temp_list:
            if item >= 0:
                item_sqrt = math.sqrt(item)

                # is_integer() работает только с типом float
                if not isinstance(item_sqrt, float):
                    item_sqrt = float(item_sqrt)

                if item_sqrt.is_integer():
                    out_list.append(int(math.sqrt(item)))

        return out_list

    print('# Задача-1')
    print(list_sqrt([2, -5, 8, 9, -25, 25, 4]))

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

def task2():

    def date_to_str(date):
        if not len(date) == 10 and not date[date.find('.', 2, 3)] == '.' and not date[date.find('.', 5, 6)] == '.':
            return False

        if date[:1] == '0':
            day = date[1:2]
        else:
            day = date[:2]

        if date[3:4] == '0':
            month = date[3:4]
        else:
            month = date[3:5]

        year = date[6:]

        import datetime
        import locale

        # Выставляем русскую дату
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

        day_list = [
            'первое',
            'второе',
            'третье',
            'четвёртое',
            'пятое',
            'шестое',
            'седьмое',
            'восьмое',
            'девятое',
            'десятое',
            'одиннадцатое',
            'двенадцатое',
            'тринадцатое',
            'четырнадцатое',
            'пятнадцатое',
            'шестнадцатое',
            'семнадцатое',
            'восемнадцатое',
            'девятнадцатое',
            'двадцатое',
            'двадцать первое',
            'двадцать второе',
            'двадцать третье',
            'двадацать четвёртое',
            'двадцать пятое',
            'двадцать шестое',
            'двадцать седьмое',
            'двадцать восьмое',
            'двадцать девятое',
            'тридцатое',
            'тридцать первое'
        ]
        date = datetime.datetime(int(year), int(month), int(day))

        return day_list[int(date.strftime('%e'))-1] + date.strftime(" %B %Y года")

    print('# Задача-2')
    print(date_to_str('02.11.2013'))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

def task3():
    import random

    print('# Задача-3')
    out_list = []
    n = input_int('Введите число элементов списка: ')

    for i in range(0, n):
        out_list.append(random.randint(-100, 100))


    print(out_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

def task4():
    print('# Задача-4')

    # а)
    lst = [1, 2, 4, 5, 6, 2, 5, 2]
    lst2 = list(set(lst))
    print('Решение а: ', end='')
    print(lst2)

    # б)
    lst = [1, 2, 4, 5, 6, 2, 5, 2]
    lst2 = set(lst)

    for item in set(lst):
        lst.remove(item)

    lst2 = list(lst2.difference(set(lst)))
    print('Решение б: ', end='')
    print(lst2)

# Демонстрация

task1()
task2()
task3()
task4()
