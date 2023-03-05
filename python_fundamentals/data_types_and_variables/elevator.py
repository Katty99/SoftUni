number_of_people = int(input())
capacity = int(input())
whole_courses = number_of_people // capacity
if number_of_people % capacity == 0:
    print(whole_courses)
else:
    total_courses = whole_courses + 1
    print(total_courses)