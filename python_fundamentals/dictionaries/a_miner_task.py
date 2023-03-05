final = {}
while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in final:
        final[resource] = 0
    final[resource] += quantity
for resource in final:
    print(f"{resource} -> {final[resource]}")