number_of_cars = int(input())
cars_dictionary = {}
for current_car in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars_dictionary[car] = [int(mileage), int(fuel)]

while True:
    command = input()
    if command == 'Stop':
        break
    if 'Drive' in command:
        drive, car, distance, fuel = command.split(' : ')
        distance = int(distance)
        fuel = int(fuel)
        if int(cars_dictionary[car][1]) >= fuel:
            cars_dictionary[car][1] -= fuel
            cars_dictionary[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars_dictionary[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            cars_dictionary.pop(car)
    elif 'Refuel' in command:
        refuel, car, fuel = command.split(' : ')
        fuel = int(fuel)
        if cars_dictionary[car][1] + fuel > 75:
            difference = 75 - cars_dictionary[car][1]
            cars_dictionary[car][1] = 75
            print(f"{car} refueled with {difference} liters")
        else:
            cars_dictionary[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif 'Revert' in command:
        revert, car, kilometers = command.split(' : ')
        kilometers = int(kilometers)
        cars_dictionary[car][0] -= kilometers
        if cars_dictionary[car][0] < 10000:
            cars_dictionary[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
for item, value in cars_dictionary.items():
    print(f"{item} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")