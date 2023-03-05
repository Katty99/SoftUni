priority_list = []
while True:
    command = input()
    if command == 'End':
        break
    split = command.split('-')
    priority = int(split[0])
    task = split[1]
    priority_list.append([priority, task])

sorted_list = []
for current_item in sorted(priority_list):
    sorted_list.append(current_item[1])
print(sorted_list)