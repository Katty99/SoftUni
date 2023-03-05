expression_1 = input()
expression_2 = input()
last_printed = expression_1
for current_letter in range(len(expression_1)):
    left_part = expression_2[:current_letter + 1]
    right_part = expression_1[current_letter + 1:]
    current_string = left_part + right_part
    if current_string == last_printed:
        continue
    print(current_string)
    last_printed = current_string