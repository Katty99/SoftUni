aimed_height = int(input())
attempt_height = aimed_height - 30
total_jumps = 0
failed_counter = 0
jumps_counter = 0
while failed_counter < 3:
    current_jump = int(input())
    while current_jump <= aimed_height:
        total_jumps += 1
        if current_jump <= attempt_height:
            failed_counter += 1
            jumps_counter += 1
        else:
            jumps_counter += 1
            attempt_height += 5
            failed_counter = 0
        total_jumps += 1
        current_jump = int(input())
    if failed_counter == 3:
        break
    break
if failed_counter == 3:
    print(f'Tihomir failed at {attempt_height}cm after {jumps_counter} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {aimed_height}cm after {total_jumps} jumps.')
