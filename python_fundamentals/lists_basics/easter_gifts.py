names_of_gifts = input().split()
command = input()
while command != 'No Money':
    current_command = command.split()
    if 'OutOfStock' in current_command:
        for index, value in enumerate(names_of_gifts):
            if value == current_command[1]:
                names_of_gifts[index] = 'None'
    elif 'Required' in current_command:
        replacing_index = int(current_command[2])
        if  replacing_index < 0 or len(names_of_gifts) < replacing_index:
            command = input()
            continue
        else:
            names_of_gifts[replacing_index] = current_command[1]
    elif 'JustInCase' in current_command:
        names_of_gifts[-1] = current_command[1]
    command = input()

while names_of_gifts.count('None') > 0:
    names_of_gifts.remove('None')
print(* names_of_gifts)

