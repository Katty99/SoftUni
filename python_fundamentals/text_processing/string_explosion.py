sequence = input()
new_text = ''
strength = 0
for index in range(len(sequence)):
    if strength > 0 and sequence[index] != '>':
        strength -= 1
    elif sequence[index] == '>':
        new_text += sequence[index]
        strength += int(sequence[index + 1])
    else:
        new_text += sequence[index]
print(new_text)