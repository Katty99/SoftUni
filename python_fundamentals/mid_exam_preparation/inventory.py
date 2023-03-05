journal = input().split(', ')
while True:
    command = input()
    if command == 'Craft!':
        break
    else:
        command = command.split(' - ')
        action = command[0]
        if action == 'Collect':
            item_collected = command[1]
            if item_collected not in journal:
                journal.append(item_collected)
        elif action == 'Drop':
            item_dropped = command[1]
            if item_dropped in journal:
                journal.remove(item_dropped)
        elif action == 'Combine Items':
            items = command[1]
            old_item, new_item = items.split(':')
            if old_item in journal:
                index = journal.index(old_item)
                new_item_index = index + 1
                journal.insert(new_item_index, new_item)
        elif action == 'Renew':
            item = command[1]
            if item in journal:
                journal.remove(item)
                journal.append(item)
print(', '.join(journal))
