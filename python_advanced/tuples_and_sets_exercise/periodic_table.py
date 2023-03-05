number_of_elements = int(input())
unique = set()
for current in range(number_of_elements):
    elements = input().split()
    for element in elements:
        unique.add(element)
for x in unique:
    print(x)