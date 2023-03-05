n = int(input())
left_sum = 0
for _ in range(1, n + 1):
    current_number = int(input())
    left_sum += current_number
right_sum = 0
for _ in range(1, n + 1):
    current_number = int(input())
    right_sum += current_number
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')
