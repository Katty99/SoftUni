budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

video_cards_price = video_cards * 250
processors_price = video_cards_price * 0.35 * processors
ram_price = video_cards_price * 0.1 * ram
total = video_cards_price + processors_price + ram_price

if video_cards > processors:
    total = total - (total * 0.15)
difference = abs(total - budget)

if budget >= total:
    print(f'You have{difference: .2f} leva left!')
else:
    print(f'Not enough money! You need{difference: .2f} leva more!')
