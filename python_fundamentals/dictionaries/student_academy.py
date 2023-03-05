pair_of_rows = int(input())
final = {}
for current_grade in range(pair_of_rows):
    student_name = input()
    student_grade = float(input())
    if student_name not in final:
        final[student_name] = []
    final[student_name].append(student_grade)
for key, value in final.items():
    average = sum(final[key]) / len(final[key])
    if average >= 4.50:
        print(f"{key} -> {average:.2f}")
