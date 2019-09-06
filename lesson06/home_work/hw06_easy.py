from components.Triangle import Triangle
from components.Trapeze import Trapeze


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
def task1():
    triangle = Triangle([1, 1], [-2, 4], [-2, -2])
    print('Сторона A: ', round(triangle.ab_side, 2))
    print('Сторона B: ', round(triangle.bc_side, 2))
    print('Сторона C: ', round(triangle.ca_side, 2))
    print('Высота: H:', round(triangle.height, 2))
    print('Площадь S:', round(triangle.square, 2))
    print('Периметр P: ', round(triangle.perimeter, 2))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
def task2():
    trapeze = Trapeze([5, 1], [0, 1], [1, 8], [8, 8])
    print('Сторона A: ', round(trapeze.ab_side, 2))
    print('Сторона B: ', round(trapeze.bc_side, 2))
    print('Сторона C: ', round(trapeze.cd_side, 2))
    print('Сторона D: ', round(trapeze.da_side, 2))
    print('Высота H:', round(trapeze.height, 2))
    print('Площадь S:', round(trapeze.square, 2))
    print('Периметр P:', round(trapeze.perimeter, 2))
    print('Равнобочная трапеция: ', 'Да' if trapeze.equal_side else 'Нет')


# Демонстрация
task1()
task2()
