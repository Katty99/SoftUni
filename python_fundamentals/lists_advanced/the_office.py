employees_happiness = input().split(' ')
improvement_factor = int(input())
happiness_as_int = [int(x) for x in employees_happiness]
mapping = [x * improvement_factor for x in happiness_as_int]
average = sum(mapping)/len(mapping)
sat_count = 0
for current_mark in mapping:
    if current_mark >= average:
        sat_count += 1
if sat_count >= len(mapping)/2:
    print(f'Score: {sat_count}/{len(mapping)}. Employees are happy!')
else:
    print(f'Score: {sat_count}/{len(mapping)}. Employees are not happy!')
    