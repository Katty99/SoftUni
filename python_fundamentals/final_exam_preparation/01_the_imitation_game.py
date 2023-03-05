encrypted_message = input()
while True:
    operation = input()
    if operation == 'Decode':
        break
    elif 'Move' in operation:
        move, number_of_letters = operation.split('|')
        number_of_letters = int(number_of_letters)
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif 'Insert' in operation:
        insert, index, value = operation.split('|')
        index = int(index)
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif 'ChangeAll' in operation:
        changeall, substring, replacement = operation.split('|')
        encrypted_message = encrypted_message.replace(substring, replacement)
print(f"The decrypted message is: {encrypted_message}")
