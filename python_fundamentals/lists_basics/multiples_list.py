factor = int(input())
count = int(input())
output_list = []
for current_number in range(1, count + 1):
    result = factor * current_number
    output_list.append(result)
print(output_list)