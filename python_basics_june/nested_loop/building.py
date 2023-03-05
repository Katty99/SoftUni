number_of_floors = int(input())
number_of_apartments = int(input())
apartment_name = ''
for floor in range(number_of_floors, 0, -1):
    for apartment in range(0, number_of_apartments):
        if floor == number_of_floors:
            apartment_name = f'L{floor * 10 + apartment}'
            print(apartment_name, end=' ')
        elif floor % 2 != 0:
            apartment_name = f'A{floor * 10 + apartment}'
            print(apartment_name, end=' ')
        else:
            apartment_name = f'O{floor * 10 + apartment}'
            print(apartment_name, end=' ')
    print()
