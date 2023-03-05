parentheses = input()
opening_parentheses = []
is_valid = True
valid_matches = '(){}[]'
for current in parentheses:
    if current in '({[':
        opening_parentheses.append(current)
    elif not opening_parentheses:
        is_valid = False
    elif current in ')}]':
        corresponding_parentheses = opening_parentheses.copy().pop()
        if f'{corresponding_parentheses + current}' not in valid_matches:
            is_valid = False
        else:
            opening_parentheses.pop()
    if not is_valid:
        break

if is_valid:
    print('YES')
else:
    print('NO')