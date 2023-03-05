number_1 = int(input())
number_2 = int(input())
operator = input()
result = 0
even_odd = ''
if operator == '+':
    result = number_1 + number_2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
elif operator == '-':
    result = number_1 - number_2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
elif operator == '*':
    result = number_1 * number_2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
elif operator == '/':
    if not number_2 == 0:
        result = number_1 / number_2
    else:
        print(f'Cannot divide {number_1} by zero')
elif operator == '%':
    if not number_2 == 0:
        result = number_1 % number_2
    else:
        print(f'Cannot divide {number_1} by zero')
if operator == '+' or operator == '-' or operator == '*':
    if even_odd == 'even':
        print(f'{number_1} {operator} {number_2} = {result} - even')
    else:
        print(f'{number_1} {operator} {number_2} = {result} - odd')
elif operator == '/':
    if not number_2 == 0:
        print(f'{number_1} {operator} {number_2} ={result: .2f}')
elif operator == '%':
    if not number_2 == 0:
        print(f'{number_1} {operator} {number_2} = {result}')
