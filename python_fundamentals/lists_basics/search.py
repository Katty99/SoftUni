number_of_lines = int(input())
word = input()
unfiltered_list = []
filtered_list = []
for current_expression in range(number_of_lines):
    expression = input()
    unfiltered_list.append(expression)
    if word in expression:
        filtered_list.append(expression)
print(unfiltered_list)
print(filtered_list)