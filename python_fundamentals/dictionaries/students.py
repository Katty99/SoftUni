students = {}
while True:
    command = input().split(':')
    if len(command) <= 1:
        break
    name = command[0]
    id = command[1]
    course = command[2]
    if course not in students.keys():
        students[course] = []
    students[course].append(f"{name} - {id}")
searched_course = command[0].replace("_", " ")
for student in students[searched_course]:
    print(student)
