# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

def task1():
    def print_vertical_list(temp_list):
        if not isinstance(temp_list, list):
            return False

        # Определяем размер отступа для выравнивания
        indent = len(max(temp_list))

        for key, value in enumerate(temp_list):
            print('{key}. '.format(key=key+1), '{value}'.format(value=value).rjust(indent))

    print('# Задача-1')
    print_vertical_list(["яблоко", "банан", "киви", "арбуз"])

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

def task2():
    def list_unique(temp1_list, temp2_list):
        if not isinstance(temp1_list, list) and not isinstance(temp2_list, list):
            return False

        temp1_list, temp2_list = set(temp1_list), set(temp2_list)
        return list(temp1_list.difference(temp2_list))

    print('# Задача-2')
    print(list_unique([1,2,2,3,3,3,4,4,4,4], [1,3,3,3,5,5,5,5,5]))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

def task3():
    def list_to(temp_list):
        if not isinstance(temp_list, list):
            return False

        out_list = []
        for item in temp_list:
            if item % 2 == 0:
                out_list.append(item/4)
            else:
                out_list.append(item*2)

        return out_list

    print('# Задача-3')
    print(list_to([1,2,2,3,3,3,4,4,4,4]))

# Демонстрация

task1()
task2()
task3()