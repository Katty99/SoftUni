def positive_negative(n):
    positive_sum = 0
    negative_sum = 0
    for num in n:
        if int(num) < 0:
            negative_sum += int(num)
        elif int(num) > 0:
            positive_sum += int(num)
    return negative_sum, positive_sum


nums = [int(x) for x in input().split()]
result = positive_negative(nums)
print(result[0])
print(result[1])
if abs(result[0]) > result[1]:
    print("The negatives are stronger than the positives")
elif abs(result[0]) < result[1]:
    print("The positives are stronger than the negatives")
