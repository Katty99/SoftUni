number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number_1 > number_3 and number_1 > number_2:
    print(number_1)
elif number_2 > number_1 and number_2 > number_3:
    print(number_2)
elif number_3 > number_1 and number_3 > number_2:
    print(number_3)