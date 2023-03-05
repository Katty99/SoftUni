cities_dictionary = {}

while True:
    command = input()
    if command == 'Sail':
        break
    city, population, gold = command.split('||')
    population = int(population)
    gold = int(gold)
    if city not in cities_dictionary:
        cities_dictionary[city] = [0, 0]
    cities_dictionary[city][0] += population
    cities_dictionary[city][1] += gold

while True:
    command = input()
    if command == 'End':
        break
    if 'Plunder' in command:
        plunder, town, population, gold = command.split('=>')
        population = int(population)
        gold = int(gold)
        cities_dictionary[town][0] -= population
        cities_dictionary[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {population} citizens killed.")
        if cities_dictionary[town][0] <= 0 or cities_dictionary[town][1] <= 0:
            cities_dictionary.pop(town)
            print(f"{town} has been wiped off the map!")
    elif 'Prosper' in command:
        prosper, town, gold = command.split('=>')
        gold = int(gold)
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            cities_dictionary[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_dictionary[town][1]} gold.")

if cities_dictionary:
    print(f"Ahoy, Captain! There are {len(cities_dictionary)} wealthy settlements to go to:")
    for city, info in cities_dictionary.items():
        print(f"{city} -> Population: {info[0]} citizens, Gold: {info[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
