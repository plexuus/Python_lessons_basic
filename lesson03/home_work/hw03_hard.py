# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def task2():
    import os

    def parse_file_to_list(path: str, re_separator: str):
        """
        Read file and content parsing
        :param path:
        :param re_separator:
        :return: list
        """
        import re

        table_list = []

        with open(path, 'r', encoding='UTF-8') as file:
            file = file.read().splitlines()

        for i in file:
            table_list.append(re.split(re_separator, i))

        return table_list

    workers_list = parse_file_to_list(os.path.join('data', 'workers'), r'\s+')
    hours_of_list = parse_file_to_list(os.path.join('data', 'hours_of'), r'\s+')

    del workers_list[0]

    for item in workers_list:
        name = f'{item[0]} {item[1]}'
        pay_per_hour = float(item[2]) / float(item[4])
        work_normal_hours = float(item[4])
        work_position = item[3]
        double_pay_per_hour = pay_per_hour * 2

        for i in hours_of_list:
            if item[0] in i and item[1] in i:
                work_hours = float(i[2])
                break
            else:
                work_hours = 0
                break

        if work_hours <= work_normal_hours:
            salary = work_hours * pay_per_hour
        elif work_hours > work_normal_hours:
            salary = work_normal_hours * pay_per_hour + (work_hours - work_normal_hours) * double_pay_per_hour
        else:
            salary = 0

        print(f'{name} ({work_position}) заработал - {round(salary)}')


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

# Демонстрация
task2()
