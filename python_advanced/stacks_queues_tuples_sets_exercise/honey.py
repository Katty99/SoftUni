from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())
total_honey = 0

functions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while nectar and working_bees:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    if current_bee > current_nectar:
        working_bees.appendleft(current_bee)
    elif current_bee < current_nectar:
        current_sign = symbols.popleft()
        total_honey += abs(functions[current_sign](current_bee, current_nectar))
print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")