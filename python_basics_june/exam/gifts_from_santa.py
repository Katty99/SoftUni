n = int(input())
m = int(input())
s = int(input())
is_special = False
for current_number in range(m, n - 1, -1):
    if current_number % 2 == 0 and current_number % 3 == 0:
        is_special = True
    else:
        continue
    if is_special and current_number == s:
        break
    if is_special:
        print(f'{current_number}', end=' ')
