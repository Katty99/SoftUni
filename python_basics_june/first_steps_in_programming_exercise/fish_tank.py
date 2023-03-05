length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage_busy = float(input())
tank_volume_in_cm = length_in_cm * width_in_cm * height_in_cm
tank_volume_in_liters = tank_volume_in_cm * 0.001
space_busy = percentage_busy / 100
needed_liters = tank_volume_in_liters * (1 - space_busy)
print(needed_liters)
