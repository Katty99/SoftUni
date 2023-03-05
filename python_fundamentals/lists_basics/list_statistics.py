number_of_inputs = int(input())
positives_list = []
negatives_list = []
for num in range(number_of_inputs):
    current_number = int(input())
    if current_number < 0:
        negatives_list.append(current_number)
    else:
        positives_list.append(current_number)
print(positives_list)
print(negatives_list)
print(f'Count of positives: {len(positives_list)}')
print(f'Sum of negatives: {sum(negatives_list)}')