import os
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir(stdin):
    if not stdin:
        print('usage: hw05_normal.py mkdir <dir_name>')
        return

    dir_path = os.path.normpath(stdin)
    name = os.path.basename(dir_path)

    try:
        os.mkdir(dir_path)
        print(f'Директория {name} создана')
    except FileExistsError:
        print(f'{name}: Директория уже существует')

if __name__ == '__main__':
    for item in range(1,9+1):
        make_dir(f'dir_{item}')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(path):
    if path is None:
        print('usage: hw05_normal.py ls <path>')
        return

    if not path:
        path = os.getcwd()

    # dir_list = sorted([item for item in os.listdir(path) if os.path.isdir(item)])
    dir_list = sorted(os.listdir(path))

    print(*dir_list, sep='\n')

if __name__ == '__main__':
    print('list_dir:')
    list_dir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(file=__file__):
    file = os.path.normpath(file)
    if not os.path.exists(file):
        return False

    file_name, file_extension = os.path.splitext(file)

    while True:
        file_name += '_copy'
        if not os.path.exists(file_name + file_extension):
            break

    shutil.copyfile(file, file_name + file_extension)

if __name__ == '__main__':
    copy_file()
