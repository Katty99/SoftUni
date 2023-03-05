animals = input().split(', ')
if animals[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    if 'wolf' in animals:
        animals.reverse()
        for index, word in enumerate(animals):
            if word == 'wolf':
                print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
