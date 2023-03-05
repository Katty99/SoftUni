number_of_students = int(input())
students_record = {}
for current_student in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in students_record:
        students_record[name] = []
    students_record[name].append(grade)

for k, v in students_record.items():
    average = sum(v) / len(v)
    print(f"{k} -> {' '.join([f'{item:.2f}' for item in v])} (avg: {average:.2f})")