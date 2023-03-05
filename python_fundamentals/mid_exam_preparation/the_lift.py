total_people = int(input())
wagons = [int(x) for x in input().split()]
final_list = []
no_more_people = False
for current_wagon in range(len(wagons)):
    while wagons[current_wagon] < 4:
        wagons[current_wagon] += 1
        total_people -= 1
        if total_people == 0:
            no_more_people = True
            break
    if no_more_people:
        break

if total_people > 0:
    print(f"There isn't enough space! {total_people} people in a queue!")
    print(*wagons)
elif total_people == 0:
    if wagons[-1] == 4:
        print(*wagons)
    else:
        print(f'The lift has empty spots!')
        print(*wagons)

