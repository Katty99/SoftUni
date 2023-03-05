sequence = input().split()
final = ''
for current in sequence:
    final += current * len(current)
print(final)