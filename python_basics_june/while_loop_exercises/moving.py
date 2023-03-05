width = int(input())
length = int(input())
height = int(input())
total_space = width * length * height
space_counter = 0
while total_space > space_counter:
    command = input()
    if command != 'Done':
        number_of_boxes = int(command)
        space_counter += number_of_boxes
    else:
        break
difference = abs(space_counter - total_space)
if total_space > space_counter:
    print(f'{difference} Cubic meters left.')
else:
    print(f'No more free space! You need {difference} Cubic meters more.')