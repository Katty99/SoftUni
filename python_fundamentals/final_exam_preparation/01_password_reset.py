password = input()
final = ''
while True:
    command = input()
    if command == 'Done':
        break

    if command == 'TakeOdd':
        for index, value in enumerate(password):
            if index % 2 != 0:
                final += password[index]
        password = final
        print(password)

    elif 'Cut' in command:
        cut, index, length = command.split(' ')
        index = int(index)
        length = int(length)
        password = password[:index] + password[index + length:]
        print(password)

    elif 'Substitute' in command:
        subs, substring, substitute = command.split(' ')
        if substring not in password:
            print("Nothing to replace!")
        else:
            password = password.replace(substring, substitute)
            print(password)
print(f"Your password is: {password}")