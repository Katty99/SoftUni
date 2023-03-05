goal = 10000
steps_counter = 0
while steps_counter < goal:
    command = input()
    if command != 'Going home':
        steps = int(command)
        steps_counter += steps
    else:
        steps_going_home = int(input())
        steps_counter += steps_going_home
        break

difference = abs(goal - steps_counter)
if steps_counter >= goal:
    print(f'Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
else:
    print(f'{difference} more steps to reach goal.')