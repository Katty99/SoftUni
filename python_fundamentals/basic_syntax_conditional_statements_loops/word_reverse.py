word = input()
reversed_word = ''
for current_letter in range(len(word) - 1, - 1, -1):
    reversed_word += word[current_letter]
print(reversed_word)