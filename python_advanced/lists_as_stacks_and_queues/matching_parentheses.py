stack = list(input())
indexes = []
for i in range(len(stack)):
    if stack[i] == '(':
        indexes.append(i)
    elif stack[i] == ')':
        print(''.join(stack[indexes.pop():i+1]))
