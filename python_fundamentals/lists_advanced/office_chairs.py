number_of_rooms = int(input())
total_chairs = 0
total_people = 0
for current_room in range(1, number_of_rooms + 1):
    chairs, people = input().split()
    total_chairs += len(chairs)
    total_people += int(people)
    diff = abs(len(chairs) - int(people))
    if int(people) > len(chairs):
        print(f'{diff} more chairs needed in room {current_room}')
total_free_chairs = total_chairs - total_people
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")