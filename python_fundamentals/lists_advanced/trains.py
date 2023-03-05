wagons = int(input())
train = [0] * wagons
while True:
    command = input()
    if command == 'End':
        break
    if 'add' in command:
        split = command.split(' ')
        action = split[0]
        number_of_people = int(split[1])
        train[-1] += number_of_people
    elif 'insert' in command:
        split = command.split(' ')
        action = split[0]
        wagon_index = int(split[1])
        number_of_people = int(split[2])
        train[wagon_index] += number_of_people
    elif 'leave' in command:
        split = command.split(' ')
        action = split[0]
        wagon_index = int(split[1])
        number_of_people = int(split[2])
        train[wagon_index] -= number_of_people

print(train)