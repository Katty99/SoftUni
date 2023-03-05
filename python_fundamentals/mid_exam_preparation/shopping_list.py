groceries = input().split('!')
while True:
    command = input()
    if command == 'Go Shopping!':
        break
    else:
        command = command.split()
        if command[0] == 'Urgent':
            if command[1] not in groceries:
                groceries.insert(0, command[1])
        elif command[0] == 'Unnecessary':
            if command[1] in groceries:
                groceries.remove(command[1])
        elif command[0] == 'Correct':
            old_item = command[1]
            new_item = command[2]
            for current_item in range(len(groceries)):
                if groceries[current_item] == old_item:
                    groceries[current_item] = new_item
        elif command[0] == 'Rearrange':
            item = command[1]
            if item in groceries:
                groceries.remove(item)
                groceries.append(item)
print(', '.join(groceries))

