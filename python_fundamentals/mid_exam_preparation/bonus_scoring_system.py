from math import ceil
number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_attendance = 0
max_bonus = 0
for current_student in range(1, number_of_students + 1):
    current_attendance = int(input())
    bonus = current_attendance / number_of_lectures * (5 + additional_bonus)
    if current_attendance > max_attendance:
        max_attendance = current_attendance
    if bonus > max_bonus:
        max_bonus = bonus
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")

