numbers = input().split(' ')
int_numbers = []
for digit in numbers:
    int_numbers.append(int(digit))
even_numbers = list(filter(lambda x: x % 2 == 0, int_numbers))
print(even_numbers)