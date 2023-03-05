input_list = input().split(' ')
abs_list = []
for current_number in input_list:
    abs_list.append(abs(float(current_number)))
print(abs_list)
