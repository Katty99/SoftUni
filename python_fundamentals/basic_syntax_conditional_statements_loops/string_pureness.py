number_of_strings = int(input())
for current_string in range(number_of_strings):
    phrase = input()
    if ',' in phrase or '.' in phrase or '_' in phrase:
        print(f'{phrase} is not pure!')
    else:
        print(f'{phrase} is pure.')