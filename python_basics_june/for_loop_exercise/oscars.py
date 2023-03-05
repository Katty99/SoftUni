actor_name = input()
points_from_academy = float(input())
jury_number = int(input())
total_points = points_from_academy

for i in range(jury_number):
    jury_name = input()
    points_from_jury = float(input())
    total_points += (len(jury_name) * points_from_jury / 2)
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    difference = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {difference:.1f} more!')
