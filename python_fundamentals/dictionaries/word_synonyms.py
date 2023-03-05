number_of_keys = int(input())
synonyms = {}
for words in range(number_of_keys):
    word = input()
    synonym = input()
    if word not in synonyms.keys():
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(f'{word} - {", ".join(synonyms[word])}')
