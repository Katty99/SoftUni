digit = int(input())
flag = False
for current_divisor in range(2, digit):
    if digit % current_divisor == 0:
        flag = True
        break
if flag:
    print('False')
else:
    print('True')