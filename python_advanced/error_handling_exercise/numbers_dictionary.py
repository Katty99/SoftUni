numbers_dictionary = {}

while True:
    num_as_text = input()
    if num_as_text == 'Search':
        break

    try:
        num = int(input())
        numbers_dictionary[num_as_text] = num

    except ValueError:
        print("The variable number must be an integer")

while True:
    searched_num = input()
    if searched_num == 'Remove':
        break

    try:
        print(numbers_dictionary[searched_num])

    except KeyError:
        print("Number does not exist in dictionary")

while True:
    searched_num = input()
    if searched_num == 'End':
        break
        
    try:
        del numbers_dictionary[searched_num]

    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)