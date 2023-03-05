day = input()

if day == 'Monday' or day == "Tuesday" or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    print(f'Working day')
elif day == 'Saturday' or day == 'Sunday':
    print(f'Weekend')
else:
    print(f'Error')