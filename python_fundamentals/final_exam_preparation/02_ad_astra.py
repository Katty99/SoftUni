import re

food_info = input()
pattern = r"(\||#)([A-Za-z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
new_list = []
calories = 0

for current in re.finditer(pattern, food_info):
    new_list.append([current.group(2), current.group(3), current.group(4)])
    calories += int(current.group(4))
days = calories // 2000

print(f"You have food to last you for: {days} days!")
for food in new_list:
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")