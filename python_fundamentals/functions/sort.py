nums = input().split(' ')
nums_to_int = []
for current_num in nums:
    nums_to_int.append(int(current_num))
print(sorted(nums_to_int))