phrase = list(input())
letters_set = set()
for letter in phrase:
    letters_set.add(letter)
for letter in sorted(letters_set):
    print(f"{letter}: {phrase.count(letter)} time/s")