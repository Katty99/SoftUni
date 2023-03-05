message = input()
while True:
    command = input()
    if command == 'Reveal':
        break
    if "InsertSpace" in command:
        insert_space, index = command.split(':|:')
        index = int(index)
        message = message[:index] + ' ' + message[index:]
    elif 'Reverse' in command:
        reverse, substring = command.split(':|:')
        if substring not in message:
            print('error')
            continue
        else:
            reversed_string = substring[::-1]
            message = message.replace(substring, '', 1)
            message += reversed_string
    elif 'ChangeAll' in command:
        change, substring, replacement = command.split(':|:')
        message = message.replace(substring, replacement)
    print(message)
print(f"You have a new text message: {message}")