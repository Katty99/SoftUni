from math import ceil
series_name = input()
episode_duration = int(input())
lunch_break = int(input())

eating_time = lunch_break * 1/8
leisure_time = lunch_break * 1/4
time_left = lunch_break - eating_time - leisure_time
difference = abs(time_left - episode_duration)

if episode_duration <= time_left:
    print(f'You have enough time to watch {series_name} and left with {ceil(difference)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(difference)} more minutes.")
