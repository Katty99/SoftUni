from collections import deque

energy = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())

total_number_of_toys = 0
total_used_energy = 0

current_elf_count = 0

while energy and materials:
    current_elf_count += 1
    current_elf = energy.popleft()
    current_material = materials.pop()

    if current_elf < 5:
        materials.append(current_material)
        continue

    if current_elf_count % 3 == 0 and current_elf_count % 5 == 0:
        if current_elf >= current_material * 2:
            total_used_energy += current_material * 2
            current_elf -= current_material * 2
            energy.append(current_elf)
        else:
            materials.append(current_material)
            current_elf *= 2
            energy.append(current_elf)
        continue

    if current_elf_count % 3 == 0:
        if current_elf >= current_material * 2:
            total_number_of_toys += 2
            total_used_energy += current_material * 2
            current_elf -= current_material * 2
            current_elf += 1
            energy.append(current_elf)

        else:
            materials.append(current_material)
            current_elf *= 2
            energy.append(current_elf)
        continue

    if current_elf_count % 5 == 0:
        if current_elf >= current_material:
            total_used_energy += current_material
            current_elf -= current_material
            energy.append(current_elf)

        else:
            materials.append(current_material)
            current_elf *= 2
            energy.append(current_elf)
        continue

    if current_elf >= current_material:
        total_number_of_toys += 1
        current_elf -= current_material
        total_used_energy += current_material
        current_elf += 1
        energy.append(current_elf)

    else:
        materials.append(current_material)
        current_elf *= 2
        energy.append(current_elf)

print(f"Toys: {total_number_of_toys}")
print(f"Energy: {total_used_energy}")

if energy:
    print(f"Elves left: {', '.join(str(x) for x in energy)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")

