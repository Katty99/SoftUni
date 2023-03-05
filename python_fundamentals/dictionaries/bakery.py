bakery = input().split()
final = {}
for x in range(0, len(bakery), 2):
    keys = bakery[x]
    values = bakery[x + 1]
    final[keys] = int(values)
print(final)


