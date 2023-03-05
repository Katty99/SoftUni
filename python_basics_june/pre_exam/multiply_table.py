number = input()
for num in range(111, int(number) + 1):
    num_to_str = str(num)
    for num3 in range(int(num_to_str[2]), int(number[2]) + 1):
        for num2 in range(int(num_to_str[1]), int(number[1]) + 1):
            for num1 in range(int(num_to_str[0]), int(number[0]) + 1):
                if num1 > 0 and num2 > 0 and num3 > 0:
                    total = num1 * num2 * num3
                    print(f'{num3} * {num2} * {num1} = {total};')

    break

