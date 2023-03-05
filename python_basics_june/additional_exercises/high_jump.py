command = int(input())
current_goal = command - 30
jumps_counter = 0
failed_counter = 0
has_succeeded = False
while failed_counter < 3:
    current_jump = int(input())
    jumps_counter += 1
    if current_jump > current_goal:
        failed_counter = 0
        current_goal += 5
    else:
        failed_counter += 1
    if current_jump > command:
        has_succeeded = True
        break
if has_succeeded:
    print(f'Tihomir succeeded, he jumped over {command}cm after {jumps_counter} jumps.')
else:
    print(f'Tihomir failed at {current_goal}cm after {jumps_counter} jumps.')
