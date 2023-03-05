processor_price_in_dollar = float(input())
video_card_price_in_dollar = float(input())
ram_price_in_dollars = float(input())
ram_quantity = int(input())
discount = float(input())
# conversion_to_lv
processor_price_in_lv = processor_price_in_dollar * 1.57
video_card_price_in_lv = video_card_price_in_dollar * 1.57
ram_price_in_lv = ram_price_in_dollars * 1.57
# discounts
processor_discounted = processor_price_in_lv - processor_price_in_lv * discount
video_card_discounted = video_card_price_in_lv - video_card_price_in_lv * discount
ram_cost = ram_price_in_lv * ram_quantity
money_needed = processor_discounted + video_card_discounted + ram_cost
print(f'Money needed - {money_needed:.2f} leva.')