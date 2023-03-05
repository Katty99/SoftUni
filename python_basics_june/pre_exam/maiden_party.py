maiden_party_price = float(input())
number_of_love_letters = int(input())
number_of_wax_roses = int(input())
number_of_keychains = int(input())
number_of_caricatures = int(input())
number_of_surprises = int(input())
total_number_of_sold_items = number_of_love_letters + number_of_wax_roses + number_of_keychains + number_of_caricatures\
                             + number_of_surprises
cost_love_letters = number_of_love_letters * 0.6
cost_of_wax_roses = number_of_wax_roses * 7.2
cost_of_keychain = number_of_keychains * 3.6
cost_of_caricatures = number_of_caricatures * 18.2
cost_of_surprises = number_of_surprises * 22
total_cost = cost_of_surprises + cost_of_caricatures + cost_of_keychain + cost_of_wax_roses + cost_love_letters
if total_number_of_sold_items >= 25:
    total_cost = total_cost - total_cost * 35 / 100
hosting_cost = total_cost * 10 / 100
final_cost = total_cost - hosting_cost
difference = abs(maiden_party_price - final_cost)
if final_cost >= maiden_party_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')

