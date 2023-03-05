sequence = [int(x) for x in input().split()]
average = sum(sequence) / len(sequence)
ready_list = []
for current_number in range(len(sequence)):
    if sequence[current_number] > average:
        ready_list.append(sequence[current_number])
        ready_list.sort(reverse=True)

if len(ready_list) == 0:
    print('No')
else:
    print(*ready_list[:5])


