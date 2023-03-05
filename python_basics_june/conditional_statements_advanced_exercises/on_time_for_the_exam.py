exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_in_minutes = exam_hour * 60 + exam_minutes
arrival_in_minutes = arrival_hour * 60 + arrival_minutes
difference = abs(arrival_in_minutes - exam_in_minutes)
difference_hours = difference // 60
difference_minutes = difference % 60

if exam_in_minutes < arrival_in_minutes:
    print(f'Late')
    if difference < 60:
        print(f'{difference} minutes after the start')
    else:
        if difference_minutes < 10:
            print(f'{difference_hours}:0{difference_minutes} hours after the start')
        else:
            print(f'{difference_hours}:{difference_minutes} hours after the start')
elif exam_in_minutes == arrival_in_minutes:
    print(f'On time')
elif difference <= 30:
    print(f'On time')
    print(f'{difference} minutes before the start')
elif difference > 30:
    print(f'Early')
    if difference < 60:
        print(f'{difference} minutes before the start')
    else:
        if difference_minutes < 10:
            print(f'{difference_hours}:0{difference_minutes} hours before the start')
        else:
            print(f'{difference_hours}:{difference_minutes} hours before the start')




