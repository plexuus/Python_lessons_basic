import math
import os
import random
import sys
import time


class LottoCLI:
    __kegs = 90  # Количество бочонков — 90 штук (с цифрами от 1 до 90)
    __card_lines = 3  # Каждая карточка содержит 3 строки
    __card_cells = 9  # Каждая карточка содержит по 9 клеток
    __card_kegs_per_line = 5  # В каждой строке по 5 случайных цифр

    def __init__(self, name):
        self.name = name[:self.__card_cells*3-2]
        self.gen_bag()  # заполняем мешок бочонками

        # Карточка игрока
        self.__player_card = self.get_card(self.bag[:])

        # Карточка компьютера
        self.__computer_card = self.get_card(self.bag[:])

    @property
    def bag(self):
        return self.__bag_list_temp

    def bag_iter(self):
        while len(self.bag) > 0:
            random_keg = random.choice(self.bag)
            self.bag.remove(random_keg)

            yield random_keg

    def check_progress(self, keg):
        # Зачеркиваем цифры у компьютера без проверок
        self.cross_count_number(self.__computer_card, keg)

        # Проверяем что выбрал игрок
        if input('Зачеркнуть цифру? (y/n) \n') == 'y':
            if not self.cross_count_number(self.__player_card, keg):
                self.print_game_over()
        else:
            if self.cross_count_number(self.__player_card, keg):
                self.print_game_over()

    def check_win(self, card: list):
        cross_count = 0

        for line in card:
            cross_count += int(line.count('--'))

        # print(f'check_win({self.__card_lines * self.__card_kegs_per_line}):{cross_count};')
        if (self.__card_lines * self.__card_kegs_per_line) > cross_count:
            return False

        return True

    @staticmethod
    def cross_count_number(card: list, number: int):
        for line in card:
            if number in line:
                card[card.index(line)][line.index(number)] = '--'
                return True

        return False

    @classmethod
    def gen_bag(cls):
        cls.__bag_list_temp = [keg for keg in range(1, cls.__kegs+1)]

    def get_card(self, kegs_list: list):
        card_list = []
        i = 0

        while i < self.__card_lines:
            line_list = []

            j = 0

            while j < self.__card_cells:
                line_list.append(random.choice(kegs_list))
                kegs_list = [i for i in kegs_list if i not in line_list]

                j += 1

            line_list.sort()

            empty_cell_list = list(range(self.__card_cells))
            random.shuffle(empty_cell_list)

            for item in empty_cell_list[:self.__card_cells - self.__card_kegs_per_line]:
                line_list[item] = '  '

            card_list.append(line_list)
            i += 1

        return card_list

    def move(self):
        keg = self.random_keg

        self.print_clear()
        self.print_card(self.__computer_card, 'Компьютер')
        self.print_card(self.__player_card, self.name)

        print(f'Новый бочонок: {keg} (осталось {len(self.bag)})')
        self.check_progress(keg)

    def print_card(self, card_list: list, owner_name: str):
        print(self.set_center_line('-' * (self.__card_cells * 3), f' {owner_name} '))

        for line in card_list:
            line = [i if len(str(i)) > 1 else f' {i}' for i in line]
            print('|'.join([str(i) for i in line]))

        print('-' * (self.__card_cells * 3))

    @staticmethod
    def print_clear():
        os.system('clear')

    @staticmethod
    def print_game_over():
        print('\n\033[91mВы проиграли\033[0m')
        exit()

    @staticmethod
    def print_progress_bar():
        i = 0
        print('Загрузка', end='')

        while i < 10:

            print('.', end='')
            sys.stdout.flush()
            time.sleep(0.2)

            i += 1

        print()

    @property
    def random_keg(self):
        return next(self.bag_iter())

    @staticmethod
    def set_center_line(line: str, string: str):
        if len(line)+1 <= len(string):
            return False

        line_center = math.floor(len(line)/2) - math.floor(len(string)/2)

        return line[:line_center] + string + line[line_center + len(string):]

    def run(self):
        self.print_clear()
        print('\033[95mИгра лото\033[0m')
        self.print_progress_bar()
        while not self.check_win(self.__computer_card) and not self.check_win(self.__player_card):
            self.move()

        if self.check_win(self.__computer_card):
            print('\n\033[91mПобедил компьютер\033[0m')

        if self.check_win(self.__player_card):
            print(f'\nПобедил \033[1m{self.name}\033[0m')
