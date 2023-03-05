number_of_commands = int(input())
cars = {}
for current_car in range(number_of_commands):
    command = input().split()
    if command[0] == 'register':
        username = command[1]
        license_plate = command[2]
        if username not in cars.keys():
            cars[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        elif username in cars.keys():
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command[0] == 'unregister':
        username = command[1]
        if username not in cars.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            cars.pop(username)
for username, license_plate in cars.items():
    print(f"{username} => {license_plate}")
