number_of_letters = int(input())
for letter_one in range(number_of_letters):
    for letter_two in range(number_of_letters):
        for letter_three in range(number_of_letters):
            print(f'{chr(letter_one + 97)}{chr(letter_two + 97)}{chr(letter_three + 97)}')
