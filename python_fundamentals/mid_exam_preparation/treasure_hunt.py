initial_loot = input().split('|')
is_empty = False
while True:
    command = input().split()
    action = command[0]
    if action == "Yohoho!":
        break
    elif action == 'Loot':
        for i in range(len(command)):
            item = command[i]
            if i == 0:
                continue
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 <= index < len(initial_loot):
            removed = initial_loot.pop(index)
            initial_loot.append(removed)
        else:
            continue

    elif action == 'Steal':
        count = int(command[1])
        if count >= len(initial_loot):
            removed = initial_loot
            is_empty = True
            print(', '.join(removed))
            print('Failed treasure hunt.')
            exit()
        else:
            removed = initial_loot[-count:]
            del initial_loot[-count:]
            print(', '.join(removed))

if len(initial_loot) > 0:
    total_letters = 0
    total_words = 0
    for i in range(len(initial_loot)):
        total_words += 1
        total_letters += len(initial_loot[i])
    average = total_letters / total_words
    print(f"Average treasure gain: {average:.2f} pirate credits.")
