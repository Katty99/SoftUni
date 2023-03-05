health = 100
bitcoins = 0
rooms = input().split('|')
rooms_count = 0
is_dead = False
for current_room in range(len(rooms)):
    current_room = rooms[current_room]
    current_room = current_room.split()
    command = current_room[0]
    num = int(current_room[1])
    rooms_count += 1
    if command == 'potion':
        if health + num <= 100:
            health += num
        else:
            num = 100 - health
            health += num
        print(f"You healed for {num} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins += num
        print(f"You found {num} bitcoins.")
    else:
        if health > num:
            health -= num
            print(f"You slayed {command}.")
        else:
            is_dead = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms_count}")
            break
if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")