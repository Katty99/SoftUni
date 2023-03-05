number_of_plants = int(input())
plants_dictionary = {}

for current_plant in range(number_of_plants):
    plant, rarity = input().split('<->')
    plants_dictionary[plant] = []
    plants_dictionary[plant].append(int(rarity))

while True:
    command = input()
    if command == 'Exhibition':
        break
    action, plant_info = command.split(': ')
    if action == 'Rate':
        plant, rating = plant_info.split(' - ')
        if plant not in plants_dictionary.keys():
            print('error')
        else:
            plants_dictionary[plant].append(int(rating))
    elif action == 'Update':
        plant, new_rarity = plant_info.split(' - ')
        if plant not in plants_dictionary.keys():
            print('error')
        else:
            plants_dictionary[plant][0] = int(new_rarity)
    elif action == 'Reset':
        plant = plant_info
        if plant not in plants_dictionary.keys():
            print('error')
        else:
            for i in range(1, len(plants_dictionary[plant])):
                plants_dictionary[plant].pop(i)

print('Plants for the exhibition:')
for item, value in plants_dictionary.items():
    if len(value) > 1:
        sum_of_ratings = 0
        length = 0
        for i in range(1, len(value)):
            sum_of_ratings += int(value[i])
            length += 1
        average = sum_of_ratings / length
        print(f"- {item}; Rarity: {value[0]}; Rating: {average:.2f}")
    else:
        print(f"- {item}; Rarity: {value[0]}; Rating: 0.00")
