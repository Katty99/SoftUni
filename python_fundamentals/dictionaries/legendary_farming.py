key_materials = {"shards": 0, "fragments": 0, "motes": 0}
materials = input().split()
is_obtained = False
while not is_obtained:
    for current in range(0, len(materials), 2):
        quantity = int(materials[current])
        material = materials[current + 1].lower()
        if material not in key_materials:
            key_materials[material] = 0
        key_materials[material] += quantity
        if key_materials['shards'] >= 250:
            print("Shadowmourne obtained!")
            key_materials["shards"] -= 250
            is_obtained = True
        elif key_materials['fragments'] >= 250:
            print("Valanyr obtained!")
            key_materials["fragments"] -= 250
            is_obtained = True
        elif key_materials['motes'] >= 250:
            print("Dragonwrath obtained!")
            key_materials["motes"] -= 250
            is_obtained = True
        if is_obtained:
            break
    if is_obtained:
        break
    materials = input().split()

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

