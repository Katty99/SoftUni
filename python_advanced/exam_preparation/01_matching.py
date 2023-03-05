from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())

matches_count = 0

while males and females:
    current_male = males.pop()
    if current_male <= 0:
        continue
    if current_male % 25 == 0:
        males.pop()
        continue

    current_female = females.popleft()
    if current_female <= 0:
        males.append(current_male)
        continue
    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)

    if current_male == current_female:
        matches_count += 1
    else:
        males.append(current_male - 2)

print(f"Matches: {matches_count}")
if males:
    reversed_males = reversed(males)
    print(f"Males left: {', '.join(str(x) for x in reversed_males)}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")

