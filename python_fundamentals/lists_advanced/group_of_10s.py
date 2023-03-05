sequence = [int(x) for x in input().split(', ')]
max_number = 0
for num in sequence:
    if int(num) > max_number:
        max_number = int(num)
number_of_groups = max_number // 10
if max_number % 10 != 0:
    number_of_groups += 1
for group in range(1, number_of_groups + 1):
    current_group = [x for x in sequence if (group - 1) * 10 < x <= group * 10]
    print(f"Group of {group * 10}'s: {current_group}")