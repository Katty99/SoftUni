sequence_1 = input().split(', ')
sequence_2 = input().split(', ')
output_list = []
for expression_1 in sequence_1:
    for expression_2 in sequence_2:
        if expression_1 in expression_2:
            output_list.append(expression_1)
            break
print(output_list)