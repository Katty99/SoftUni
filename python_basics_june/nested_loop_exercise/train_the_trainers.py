number_of_jury = int(input())
presentation_name = input()
number_of_presentations = 0
final_average_grade = 0
while presentation_name != 'Finish':
    number_of_presentations += 1
    current_presentation_grade = 0
    for grade in range(1, number_of_jury + 1):
        current_grade = float(input())
        current_presentation_grade += current_grade
        average_exam = current_presentation_grade / number_of_jury
    final_average_grade += average_exam
    print(f'{presentation_name} - {average_exam:.2f}.')
    presentation_name = input()
final_average_grade /= number_of_presentations
print(f"Student's final assessment is {final_average_grade:.2f}.")
