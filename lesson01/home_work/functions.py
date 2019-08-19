from os import path

def home_work_greet(author, home_work_name):
    home_work_name = path.basename(home_work_name)

    print(
        'Welcome to ',
        home_work_name[:home_work_name.index('.py')],
        '\n',
        'Author: ',
        author,
        '\n',
        sep=''
    )

def input_int(prompt, error_message=''):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            if error_message:
                print(error_message)
            continue

def input_float(prompt, error_message=''):
    while True:
        try:
            if is_print:
                print(float(input(prompt)))
                return

            return float(input(prompt))
        except ValueError:
            if error_message:
                print(error_message)
            continue