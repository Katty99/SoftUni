from collections import deque

substring = deque(input().split())
colours_received = []

main_colours = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}
secondary_colours = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'blue', 'yellow'}
}

while substring:
    first = substring.popleft()
    second = substring.pop() if substring else ''
    for colour in (first + second, second + first):
        if colour in main_colours:
            colours_received.append(colour)
            break
    else:
        for el in (first[:-1], second[:-1]):
            if el:
                middle = len(substring) // 2
                substring.insert(middle, el)

for colour in set(secondary_colours.keys()).intersection(colours_received):
    if not secondary_colours[colour].issubset(colours_received):
        colours_received.remove(colour)

print(colours_received)