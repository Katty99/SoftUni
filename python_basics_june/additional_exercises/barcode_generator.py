first_number = input()
second_number = input()
for num in range(int(first_number[0]), int(second_number[0]) + 1):
    for num1 in range(int(first_number[1]), int(second_number[1]) + 1):
        for num2 in range(int(first_number[2]), int(second_number[2]) + 1):
            for num3 in range(int(first_number[3]), int(second_number[3]) + 1):
                if num % 2 != 0 and num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0:
                    print(f'{num}{num1}{num2}{num3}', end=' ')

