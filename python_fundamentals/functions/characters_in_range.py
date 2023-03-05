def char_range(char_1, char_2):
    list_of_chars = []
    for current_char in range(ord(char_1) + 1, ord(char_2)):
        list_of_chars.append(chr(current_char))
    return list_of_chars


first_char = input()
second_char = input()
print(*(char_range(first_char, second_char)))