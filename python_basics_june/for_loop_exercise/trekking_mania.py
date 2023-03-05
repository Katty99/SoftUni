number_of_groups = int(input())
musala_climbers = 0
montblanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for _ in range(number_of_groups):
    number_of_people_in_a_group = int(input())
    if number_of_people_in_a_group <= 5:
        musala_climbers += number_of_people_in_a_group
    elif number_of_people_in_a_group <= 12:
        montblanc_climbers += number_of_people_in_a_group
    elif number_of_people_in_a_group <= 25:
        kilimanjaro_climbers += number_of_people_in_a_group
    elif number_of_people_in_a_group <= 40:
        k2_climbers += number_of_people_in_a_group
    else:
        everest_climbers += number_of_people_in_a_group
total_climbers = musala_climbers + montblanc_climbers + kilimanjaro_climbers + k2_climbers + everest_climbers
percentage_musala_climbers = musala_climbers / total_climbers * 100
percentage_montblanc_climbers = montblanc_climbers / total_climbers * 100
percentage_kilimanjaro_climbers = kilimanjaro_climbers / total_climbers * 100
percentage_k2_climbers = k2_climbers / total_climbers * 100
percentage_everest_climbers = everest_climbers / total_climbers * 100
print(f'{percentage_musala_climbers:.2f}%')
print(f'{percentage_montblanc_climbers:.2f}%')
print(f'{percentage_kilimanjaro_climbers:.2f}%')
print(f'{percentage_k2_climbers:.2f}%')
print(f'{percentage_everest_climbers:.2f}%')