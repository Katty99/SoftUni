# reading the searched words and the text
with open('words.txt', 'w') as words_file:
    words = input().split()
    for current_word in words:
        words_file.write(f'{current_word} \n')

with open('text.txt', 'w') as text_file:
    while True:
        line = input().lower()
        if line == '':
            break
        text_file.write(f"{line} \n")

# checking the texts
matches = {}

for word in open('words.txt', 'r'):
    word = word.split()
    searched = word[0]
    for text in open('text.txt', 'r'):
        if searched in text:
            if searched not in matches:
                matches[searched] = 0
            matches[searched] += 1


to_print = sorted(matches.items(), key=lambda x: -x[1])
for key, value in to_print:
    print(f"{key} - {value}")