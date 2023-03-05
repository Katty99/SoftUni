expression = input()
for index in range(len(expression)):
    if expression[index] == ':':
        print(f"{expression[index]}{expression[index + 1]}")