final = {}
while True:
    command = input()
    if command == 'end':
        break
    course_name, student_name = command.split(' : ')
    if course_name not in final:
        final[course_name] = []
    final[course_name].append(student_name)

for course_name, student_name in final.items():
    print(f"{course_name}: {len(final[course_name])}")
    for student in final[course_name]:
        print(f"-- {student}")