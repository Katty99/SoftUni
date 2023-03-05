animal = input()

if animal == 'dog':
    print(f'mammal')
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    print(f'reptile')
else:
    print(f'unknown')