from math import ceil
from math import floor
racket_price = float(input())
number_of_rackets = int(input())
number_of_shoes_pairs = int(input())
rackets_cost = racket_price * number_of_rackets
shoes_price = racket_price / 6
shoes_cost = shoes_price * number_of_shoes_pairs
cost_for_other_equipment = (rackets_cost + shoes_cost) * 20 / 100
total_sum = rackets_cost + shoes_cost + cost_for_other_equipment
amount_paid_by_djokovic = total_sum / 8
amount_paid_by_sponsors = total_sum * 7 / 8
print(f'Price to be paid by Djokovic {floor(amount_paid_by_djokovic)}')
print(f'Price to be paid by sponsors {ceil(amount_paid_by_sponsors)}')

