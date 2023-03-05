from collections import deque

materials = deque(int(x) for x in input().split(' '))
magic = deque(int(x) for x in input().split(' '))

presents = {
    'Gemstone': [100, 200],
    'Porcelain Sculpture': [200, 300],
    'Gold': [300, 400],
    'Diamond Jewellery': [400, 500]
}

gifts_made = {}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    current_sum = current_material + current_magic
    if current_sum < 100:
        if current_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            current_sum = current_material + current_magic
        else:
            current_sum *= 2

    elif current_sum > 499:
        current_sum /= 2

    for present, value in presents.items():
        if int(current_sum) in range(value[0], value[1]):
            if present not in gifts_made:
                gifts_made[present] = 0
            gifts_made[present] += 1

success = False
if ('Gemstone' in gifts_made and 'Porcelain Sculpture' in gifts_made) or \
    ('Diamond Jewellery' in gifts_made and 'Gold' in gifts_made):
    success = True

if success:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in sorted(gifts_made.items()):
    if value:
        print(f"{key}: {value}")