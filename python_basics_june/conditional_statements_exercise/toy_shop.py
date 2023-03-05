vacation_price = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

puzzle_price = puzzle * 2.6
doll_price = doll * 3
bear_price = bear * 4.1
minion_price = minion * 8.20
truck_price = truck * 2

total_purchased_units = puzzle + doll + bear + minion + truck
total_revenues = puzzle_price + doll_price + bear_price + minion_price + truck_price
if total_purchased_units >= 50:
    total_revenues = total_revenues - (total_revenues * 0.25)
else:
    total_revenues = total_revenues

rent = total_revenues * 0.1
income = total_revenues - rent

difference = abs(income - vacation_price)

if income >= vacation_price:
    print(f'Yes!{difference: .2f} lv left.')
else:
    print(f'Not enough money!{difference: .2f} lv needed.')
