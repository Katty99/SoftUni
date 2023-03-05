from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
presents = {
    '150': 'Doll',
    '250': 'Wooden train',
    '300': 'Teddy bear',
    '400': 'Bicycle'
}
manufactured = {}

while magic and materials:
    current_material = materials.pop()
    current_magic = magic.popleft()
    result = current_magic * current_material
    if str(result) in presents.keys():
        present = presents[str(result)]
        if present not in manufactured:
            manufactured[present] = 0
        manufactured[present] += 1
        continue
    if result < 0:
        materials.append(current_material + current_magic)
    elif result > 0:
        materials.append(current_material + 15)
    else:
        if current_magic != 0:
            magic.appendleft(current_magic)
        elif current_material != 0:
            materials.append(current_material)

success_1 = {'Doll', 'Wooden train'}
success_2 = {'Teddy bear', 'Bicycle'}

if success_1.issubset(manufactured) or success_2.issubset(manufactured):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for toy, amount in sorted(manufactured.items()):
    print(f"{toy}: {amount}")