string = input()
digits = ''
letters = ''
characters = ''
for character in string:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        letters += character
    else:
        characters += character
print(digits)
print(letters)
print(characters)