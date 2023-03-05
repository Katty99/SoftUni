number_of_days_off = int(input())
number_of_working_days = 365 - number_of_days_off
total_play_time = number_of_working_days * 63 + number_of_days_off * 127
difference = abs(total_play_time - 30000)
total_play_time_hours = difference // 60
total_play_time_minutes = difference % 60
if total_play_time <= 30000:
    print(f'Tom sleeps well')
    print(f'{total_play_time_hours} hours and {total_play_time_minutes} minutes less for play')
else:
    print(f'Tom will run away')
    print(f'{total_play_time_hours} hours and {total_play_time_minutes} minutes more for play')