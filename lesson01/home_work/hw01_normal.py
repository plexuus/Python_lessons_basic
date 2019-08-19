try:
    from .functions import *
except ImportError:
    from lesson01.home_work.functions import *

__author__ = 'Tokarev Artem'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

def task1():
    def max_numeral(number):
        i, j = 0, 0
        number = str(abs(number))

        while i < len(number):
            if int(number[i]) > int(j):
                j = number[i]
            i += 1

        return j

    print('# Задача-1')
    print('Самая большая цифра:', max_numeral(input_int('Введите целое число: ')))


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

def task2():
    def set_var():
        input_var_a = input('Введите переменную а: ')
        input_var_b = input('Введите переменную b: ')

        return input_var_a, input_var_b

    def change_var(a, b):
        var_a = str(b) + str(a)
        var_b = a
        var_a = var_a[:var_a.index(var_b)]

        return var_a, var_b

    print('# Задача-2')
    var_a, var_b = set_var()
    new_var_a, new_var_b = change_var(var_a, var_b)
    print('Результат: теперь переменная a = ', new_var_a, '; ', 'переменная b = ', new_var_b, ';', sep='')


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

def task3():
    import math

    a = input_float('Введите число а: ')
    b = input_float('Введите число b: ')
    c = input_float('Введите число c: ')

    # Дискриминант
    d = b ** 2 - 4 * a * c

    if d > 0:

        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)

        print("x1 = ", x1, " x2 = ", x2)

    elif d == 0:

        x1 = -(b / (2 * a))
        print("x1 и x2= ", x1)


    else:
        print("Нет действительных корней")


# Демонстрация
home_work_greet(__author__, __file__)
task1()
task2()
task3()