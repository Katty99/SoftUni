def operate(operator, *nums):
    result = nums[0]
    if operator == '+':
        for num in nums[1:]:
            result += num

    elif operator == '-':
        for num in nums[1:]:
            result -= num

    elif operator == '*':
        for num in nums[1:]:
            result *= num

    elif operator == '/':
        for num in nums[1:]:
            result /= num
    return result


print(operate("*", 3, 4))
