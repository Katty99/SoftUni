country = input()
equipment = input()
if country == 'Russia':
    if equipment == 'ribbon':
        difficulty = 9.1
        performance = 9.4
    elif equipment == 'hoop':
        difficulty = 9.3
        performance = 9.8
    else:
        difficulty = 9.6
        performance = 9
elif country == 'Bulgaria':
    if equipment == 'ribbon':
        difficulty = 9.6
        performance = 9.4
    elif equipment == 'hoop':
        difficulty = 9.55
        performance = 9.75
    else:
        difficulty = 9.5
        performance = 9.4
else:
    if equipment == 'ribbon':
        difficulty = 9.2
        performance = 9.5
    elif equipment == 'hoop':
        difficulty = 9.45
        performance = 9.35
    else:
        difficulty = 9.7
        performance = 9.15
final_grade = difficulty + performance
insufficient_points = 20 - final_grade
percentage_insufficiency = insufficient_points / 20 * 100
print(f'The team of {country} get {final_grade:.3f} on {equipment}.')
print(f'{percentage_insufficiency:.2f}%')
