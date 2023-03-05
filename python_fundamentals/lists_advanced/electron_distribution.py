number_of_electrons = int(input())
distributed = []
shell_number = 0
while number_of_electrons > 0:
    shell_number += 1
    shell_capacity = 2 * shell_number ** 2
    if shell_capacity > number_of_electrons:
        distributed.append(number_of_electrons)
        number_of_electrons = 0
        break
    distributed.append(shell_capacity)
    number_of_electrons -= shell_capacity

print(distributed)