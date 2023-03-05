string = input()
final = ''
last_used = ''
for char in string:
    if char not in last_used:
        final += char
        last_used = char
print(final)