from collections import deque

textiles = deque(int(x) for x in input().split())
meds = deque(int(x) for x in input().split())

items = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100
}

created = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while textiles and meds:
    current_textile = textiles.popleft()
    current_med = meds.pop()
    current_sum = current_med + current_textile
    values = [30, 40, 100]

    if current_sum in values:
        for key, value in items.items():
            if value == current_sum:
                created[key] += 1

    elif current_sum > items['MedKit']:
        created['MedKit'] += 1
        remainder = meds.pop()
        remainder += current_sum - 100
        meds.append(remainder)

    else:
        current_med += 10
        meds.append(current_med)

if not textiles and not meds:
    print("Textiles and medicaments are both empty.")
elif not textiles and meds:
    print("Textiles are empty.")
elif textiles and not meds:
    print("Medicaments are empty.")

for key, value in sorted(created.items(), key=lambda x: (-x[1], x[0])):
    if value:
        print(f"{key} - {value}")

if meds:
    reverse = reversed(meds)
    print(f"Medicaments left: {', '.join(str(x) for x in reverse)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")