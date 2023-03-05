activation_key = input()
while True:
    command = input()
    if command == 'Generate':
        break
    if 'Contains' in command:
        contains, substring = command.split(">>>")
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif 'Flip' in command:
        flip, upper_lower, start, end = command.split(">>>")
        start = int(start)
        end = int(end)
        to_replace = ''
        result = ''
        for i in range(start, end):
            to_replace += activation_key[i]
            if upper_lower == 'Upper':
                result += activation_key[i].upper()
            elif upper_lower == 'Lower':
                result += activation_key[i].lower()
        activation_key = activation_key.replace(to_replace, result)
        print(activation_key)
    elif 'Slice' in command:
        action, start, end = command.split(">>>")
        start = int(start)
        end = int(end)
        activation_key = activation_key[:start] + activation_key[end:]
        print(activation_key)
print(f'Your activation key is: {activation_key}')