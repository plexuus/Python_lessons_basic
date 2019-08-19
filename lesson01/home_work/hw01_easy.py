try:
    from .functions import *
except ImportError:
    from lesson01.home_work.functions import *

__author__ = 'Tokarev Artem'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

def task1():
    def print_numeral_step_one(value):
        import time, sys

        value = str(abs(value))
        i = 0

        while i < len(value):
            print(value[i], end=' ')
            i += 1

            # Вывод в консоль с задержкой
            sys.stdout.flush()
            time.sleep(0.2)

        print('')

    print('# Задача-1')
    print('Результат: ', end='')
    print_numeral_step_one(input_int('Введите целое число: ', 'ОШИБКА ВВОДА'))


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

def task2():
    def set_var():
        input_var_a = input('Введите переменную а: ')
        input_var_b = input('Введите переменную b: ')

        return input_var_a, input_var_b

    def change_var(var_a, var_b):
        var_c = var_a
        var_a = var_b
        var_b = var_c

        return var_a, var_b

    print('# Задача-2')
    var_a, var_b = set_var()
    new_var_a, new_var_b = change_var(var_a, var_b)
    print('Результат: теперь переменная a = ', new_var_a, '; ', 'переменная b = ', new_var_b, ';', sep='')


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

def task3():
    def age_verification():
        age = input_int('Введите свой возраст: ')

        if age >= 18:
            print('Доступ разрешен')
        else:
            print('Извините, пользование данным ресурсом только с 18 лет')

    print('# Задача-3')
    age_verification()

# Демонстрация
home_work_greet(__author__, __file__)
task1()
task2()
task3()