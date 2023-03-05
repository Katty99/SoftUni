numbers_list = input().split(', ')
even_nums = [i for i, x in enumerate(numbers_list) if int(x) % 2 == 0]
print(even_nums)

