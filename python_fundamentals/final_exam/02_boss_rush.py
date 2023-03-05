import re

num = int(input())
for i in range(num):
    boss_title = input()
    pattern = r'\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#'
    match = re.search(pattern, boss_title)
    if not match:
        print("Access denied!")
        continue
    boss_name = match.group(1)
    title = match.group(2)
    print(f"{boss_name}, The {title}")
    print(f">> Strength: {len(boss_name)}")
    print(f">> Armor: {len(title)}")