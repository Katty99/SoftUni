time_per_walk = int(input())
number_of_walks = int(input())
calories_intake = int(input())
calories_burnt = time_per_walk * number_of_walks * 5
if calories_burnt >= calories_intake / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.')