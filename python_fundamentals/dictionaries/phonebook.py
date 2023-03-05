phonebook = {}
while True:
    command = input()
    if '-' not in command:
        break
    name, number = command.split('-')
    phonebook[name] = number
for current in range(int(command)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")