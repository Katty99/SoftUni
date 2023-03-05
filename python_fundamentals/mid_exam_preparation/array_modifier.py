array = [int(x) for x in input().split()]

while True:
    command = input().split()
    if command[0] == 'end':
        break
    elif command[0] == 'swap':
        index_1 = int(command[1])
        index_2 = int(command[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]
    elif command[0] == 'multiply':
        index_1 = int(command[1])
        index_2 = int(command[2])
        array[index_1] *= array[index_2]
    elif command[0] == 'decrease':
        for current_element in range(len(array)):
            array[current_element] -= 1
print(*array, sep=', ')
