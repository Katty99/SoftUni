from math import floor
from math import ceil
number_of_painting_boxes = int(input())
number_of_wallpapers = int(input())
gloves_price = float(input())
brush_price = float(input())
painting_cost = number_of_painting_boxes * 21.5
wallpapers_cost = number_of_wallpapers * 5.2
number_of_gloves_needed = ceil(number_of_wallpapers * 35 / 100)
number_of_brushes_needed = floor(number_of_painting_boxes * 48 / 100)
gloves_cost = gloves_price * number_of_gloves_needed
brush_cost = brush_price * number_of_brushes_needed
total_cost = painting_cost + wallpapers_cost + gloves_cost + brush_cost
delivery_cost = total_cost / 15
total_sum = total_cost + delivery_cost
print(f'This delivery will cost {delivery_cost:.2f} lv.')
