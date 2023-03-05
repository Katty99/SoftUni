type_value_fire = input().split('#')
water = int(input())
total_fire_counter = 0
total_effort_counter = 0
valid_list = []

for current_fire in type_value_fire:
    fire_level = current_fire.split('=')
    if int(fire_level[1]) > water:
        continue
    if 'Low' in current_fire:
        if 1 <= int(fire_level[1]) <= 50:
            total_fire_counter += int(fire_level[1])
            total_effort_counter += int(fire_level[1]) * 0.25
            water -= int(fire_level[1])
            valid_list.append(fire_level[1])
        else:
            continue
    elif 'Medium' in current_fire:
        if 51 <= int(fire_level[1]) <= 80:
            total_fire_counter += int(fire_level[1])
            total_effort_counter += int(fire_level[1]) * 0.25
            water -= int(fire_level[1])
            valid_list.append(fire_level[1])
        else:
            continue
    elif 'High' in current_fire:
        if 81 <= int(fire_level[1]) <= 125:
            total_fire_counter += int(fire_level[1])
            total_effort_counter += int(fire_level[1]) * 0.25
            water -= int(fire_level[1])
            valid_list.append(fire_level[1])
        else:
            continue
    else:
        continue

print('Cells:')
for current_count in valid_list:
    print(f'-{current_count}')
print(f'Effort: {total_effort_counter:.2f}')
print(f'Total Fire: {total_fire_counter}')
