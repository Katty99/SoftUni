number_of_bad_grades = int(input())
bad_grades_counter = 0
total_problems = 0
average_grade = 0
is_expelled = False
last_problem = ''
command = input()
while command != 'Enough':
    grade = int(input())
    if grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == number_of_bad_grades:
            is_expelled = True
            break

    total_problems += 1
    last_problem = command
    command = input()
    average_grade += grade

if is_expelled:
    print(f'You need a break, {bad_grades_counter} poor grades.')
if not is_expelled:
    print(f'Average score: {average_grade / total_problems :.2f}')
    print(f'Number of problems: {total_problems}')
    print(f'Last problem: {last_problem}')


