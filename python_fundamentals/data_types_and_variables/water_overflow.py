tank_capacity = 255
number_of_pours = int(input())
water_liters_counter = 0
for current_liters in range(number_of_pours):
    liters_of_water = int(input())
    if water_liters_counter + liters_of_water > tank_capacity:
        print("Insufficient capacity!")
        continue
    water_liters_counter += liters_of_water
print(water_liters_counter)