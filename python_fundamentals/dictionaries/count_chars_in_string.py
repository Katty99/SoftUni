characters = input()
no_space = [x for x in characters if x != ' ']
final = {}
for char in no_space:
    if char not in final:
        final[char] = 0
    final[char] += 1

for key in final:
    print(f"{key} -> {final[key]}")