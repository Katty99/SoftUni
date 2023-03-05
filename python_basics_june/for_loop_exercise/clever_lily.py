years = int(input())
laundry_price = float(input())
toys_price = int(input())
total_money = 0
total_toys = 0
current_birthday_money = 0
for i in range(1, years + 1):
    if i % 2 == 0:
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else:
        total_toys += 1
total_money += total_toys * toys_price
difference = abs(total_money - laundry_price)
if total_money >= laundry_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
