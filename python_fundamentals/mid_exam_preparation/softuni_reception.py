employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students_count = int(input())
hours = 0
total_students_per_hour = employee_1 + employee_2 + employee_3
while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    else:
        students_count -= total_students_per_hour
print(f'Time needed: {hours}h.')