file = open('numbers.txt', 'r')
total = 0
for line in file:
    total += int(line)

print(total)