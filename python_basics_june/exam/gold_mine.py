number_of_locations = int(input())
for current_location in range(number_of_locations):
    average_expected = float(input())
    number_of_days = int(input())
    total_gold = 0
    for current_day in range(number_of_days):
        gold_extracted = float(input())
        total_gold += gold_extracted
    average_extracted = total_gold / number_of_days
    difference = abs(average_extracted - average_expected)
    if total_gold / number_of_days >= average_expected:
        print(f'Good job! Average gold per day: {average_extracted:.2f}.')
    else:
        print(f'You need {difference:.2f} gold.')