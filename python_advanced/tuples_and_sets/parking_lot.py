number_of_commands = int(input())
car_info = set()
for current in range(number_of_commands):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        car_info.add(car_number)
    else:
        if car_info:
            car_info.remove(car_number)
        else:
            continue
if car_info:
    for car in car_info:
        print(car)
else:
    print("Parking Lot is Empty")