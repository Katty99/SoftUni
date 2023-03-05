current_month = input()
number_of_hours = int(input())
number_of_people = int(input())
time_of_the_day = input()
if current_month == 'march' or current_month == 'april' or current_month == 'may':
    if time_of_the_day == 'day':
        cost_per_person = number_of_hours * 10.5
    else:
        cost_per_person = number_of_hours * 8.4
else:
    if time_of_the_day == 'day':
        cost_per_person = number_of_hours * 12.6
    else:
        cost_per_person = number_of_hours * 10.2

if number_of_people >= 4:
    cost_per_person -= cost_per_person * 10 / 100
if number_of_hours >= 5:
    cost_per_person -= cost_per_person * 50 / 100

print(f'Price per person for one hour: {cost_per_person / number_of_hours:.2f}')
print(f'Total cost of the visit: {cost_per_person * number_of_people:.2f}')