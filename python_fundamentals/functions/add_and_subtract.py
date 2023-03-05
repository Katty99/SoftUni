def sum_numbers(number_1, number_2):
    return number_1 + number_2


def subtract(sum, number_3):
    return sum - number_3


def add_and_subtract(number_1, number_2, number_3):
    sum_of_first_two = number_1 + number_2
    result = subtract(sum_of_first_two, number_3)
    return result


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(add_and_subtract(num_one, num_two, num_three))