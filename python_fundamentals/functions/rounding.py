numbers_to_round = input().split(' ')
rounded_list = []
for current_number in numbers_to_round:
    rounded_list.append(round(float(current_number)))
print(rounded_list)