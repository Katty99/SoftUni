from collections import deque

vowels = deque(x for x in input().split())
consonants = deque(x for x in input().split())

valid_words = {'rose': 'rose', 'tulip': 'tulip', 'lotus': 'lotus', 'daffodil': 'daffodil'}
not_found = True

while vowels and consonants and not_found:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for word in valid_words.keys():
        valid_words[word] = valid_words[word].replace(vowel, '')
        valid_words[word] = valid_words[word].replace(consonant, '')
        if valid_words[word] == '':
            print(f"Word found: {word}")
            not_found = False
            break

if not_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(x for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(x for x in consonants)}")
