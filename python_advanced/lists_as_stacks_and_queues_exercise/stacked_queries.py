lines = int(input())
stack = []
for current in range(lines):
    command = input()
    if '1' in command:
        action, num = command.split(' ')
        stack.append(int(num))
    elif command == '2':
        if stack:
            stack.pop()
        else:
            pass
    elif command == '3':
        if stack:
            print(max(stack))
        else:
            pass
    elif command == '4':
        if stack:
            print(min(stack))
        else:
            pass

stack.reverse()
print(*stack, sep=', ')
