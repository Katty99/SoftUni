words = input().split()
dictionary = {}
for x in words:
    lower = x.lower()
    if lower not in dictionary.keys():
        dictionary[lower] = 0
    dictionary[lower] += 1
for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')
