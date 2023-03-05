import os


def create_file(file_name):
    open(f"files/{file_name}", 'w')


def add(file_name, content):
    with open(f'files/{file_name}', 'a') as file:
        file.write(f'{content}\n')


def replace(file_name, old, new):
    try:
        with open(f'files/{file_name}', 'r') as file:
            text = file.read()
            text = text.replace(old, new)

        with open(f'files/{file_name}', 'w') as file:
            file.write(text)

    except FileNotFoundError:
        print("An error occurred")


def delete(file_name):
    try:
        os.remove(f'files/{file_name}')
    except FileNotFoundError:
        print('An error occurred')


while True:
    command = input()
    if command == 'End':
        break
    command = command.split('-')
    action = command[0]
    if action == 'Create':
        create_file(command[1])
    elif action == 'Add':
        add(command[1], command[2])
    elif action == 'Replace':
        replace(command[1], command[2], command[3])
    elif action == 'Delete':
        delete(command[1])
