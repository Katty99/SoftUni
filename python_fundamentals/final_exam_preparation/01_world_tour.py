stops = input()
while True:
    command = input()
    if command == 'Travel':
        break
    action, start, end = command.split(':')
    if action == 'Add Stop':
        index = int(start)
        if index >= len(stops):
            print(stops)
            continue
        else:
            stops = stops[:index] + end + stops[index:]
            print(stops)
    elif action == 'Remove Stop':
        start = int(start)
        end = int(end)
        if start not in range(len(stops)) or end not in range(len(stops)):
            print(stops)
            continue
        else:
            stops = stops[:start] + stops[end + 1:]
            print(stops)
    elif action == 'Switch':
        if start not in stops:
            print(stops)
            continue
        else:
            count = stops.count(start)
            stops = stops.replace(start, end, count)
            print(stops)
print(f"Ready for world tour! Planned stops: {stops}")