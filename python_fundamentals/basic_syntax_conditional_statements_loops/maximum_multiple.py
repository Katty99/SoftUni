divisor = int(input())
boundary = int(input())
largest_number = 0
for current_number in range(boundary, divisor, -1):
    if current_number % divisor != 0:
        continue
    if current_number % divisor > boundary:
        continue
    if current_number % divisor == 0:
        largest_number = current_number
        print(largest_number)
        break