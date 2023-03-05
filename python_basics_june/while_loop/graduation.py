name = input()
grades_counter = 0
years_counter = 0
failed_counter = 0
while True:
    grade = float(input())
    years_counter += 1
    if grade >= 4:
        grades_counter += grade

    else:
        failed_counter += 1
        if failed_counter == 2:
            print(f'{name} has been excluded at {years_counter} grade')
            break
        years_counter -= 1

    if years_counter == 12:
        average_grade = grades_counter / years_counter
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break
