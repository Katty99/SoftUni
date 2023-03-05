number = int(input())
for num in range (0, number + 1):
    if num % 2 == 0:
        result = 2 ** num
        print(f'{result}')
