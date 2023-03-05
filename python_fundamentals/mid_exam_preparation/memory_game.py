sequence = input().split()
number_of_tries = 0
while True:
    command = input()
    if command == 'end':
        if len(sequence) > 0:
            print('Sorry you lose :(')
            print(*sequence)
        break
    if len(sequence) == 0:
        continue
    choice_1, choice_2 = command.split()
    choice_1 = int(choice_1)
    choice_2 = int(choice_2)
    number_of_tries += 1
    if choice_1 < 0 or choice_2 < 0 or choice_1 == choice_2 or len(sequence) - 1 < choice_1 or\
            len(sequence) - 1 < choice_2:
        middle = len(sequence) // 2
        sequence[middle:middle] = [f'-{number_of_tries}a'] * 2
        print('Invalid input! Adding additional elements to the board')
    elif sequence[choice_1] == sequence[choice_2]:
        print(f'Congrats! You have found matching elements - {sequence[choice_1]}!')
        sequence = [x for x in sequence if x not in (sequence[choice_1])]
    else:
        print('Try again!')
    if len(sequence) == 0:
        print(f'You have won in {number_of_tries} turns!')
        continue
        