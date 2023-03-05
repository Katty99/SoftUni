while True:
    command = input()
    word = ''
    if command == 'End':
        break
    if command == 'SoftUni':
        continue
    for char in command:
        word += 2 * char
    print(word)


