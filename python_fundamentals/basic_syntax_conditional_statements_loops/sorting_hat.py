command = input()
team = ''
while command != 'Welcome!':
    if command == 'Voldemort':
        print('You must not speak of that name!')
        break
    if len(command) < 5:
        team = 'Gryffindor'
    elif len(command) == 5:
        team = 'Slytherin'
    elif len(command) == 6:
        team = 'Ravenclaw'
    else:
        team = 'Hufflepuff'
    print(f'{command} goes to {team}.')
    command = input()
if command == 'Welcome!':
    print('Welcome to Hogwarts.')
