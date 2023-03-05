word = input()
sum_of_vowels = 0
for i in range(0, len(word)):
    if word[i] == 'a':
        sum_of_vowels += 1
    if word[i] == 'e':
        sum_of_vowels += 2
    if word[i] == 'i':
        sum_of_vowels += 3
    if word[i] == 'o':
        sum_of_vowels += 4
    if word[i] == 'u':
        sum_of_vowels += 5
print(sum_of_vowels)
