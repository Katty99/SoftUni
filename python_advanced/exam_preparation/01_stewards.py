from collections import deque

seats = input().split(', ')
first_sequence = deque(int(x) for x in input().split(', '))
second_sequence = deque(int(x) for x in input().split(', '))

matches = []
seats_matched = 0
rotations = 0

while seats_matched < 3 and rotations < 10:
    first = first_sequence.popleft()
    second = second_sequence.pop()
    current_letter = chr(first + second)
    first_try = f"{first}{current_letter}"
    second_try = f"{second}{current_letter}"

    if first_try in seats:
        seats.remove(first_try)
        seats_matched += 1
        matches.append(first_try)
    elif second_try in seats:
        seats.remove(second_try)
        seats_matched += 1
        matches.append(second_try)
    else:
        first_sequence.append(first)
        second_sequence.appendleft(second)
    rotations += 1

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotations}")