nums = input().split(' ')
nums_to_int = []
for current_num in nums:
    nums_to_int.append(int(current_num))
print(f"The minimum number is {min(nums_to_int)}")
print(f"The maximum number is {max(nums_to_int)}")
print(f'The sum number is: {sum(nums_to_int)}')