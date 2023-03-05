square_meters = float(input())
cost = square_meters * 7.61
discount = cost * 0.18
final_price = cost - discount
print(f'The final price is {final_price} lv.')
print(f'The discount is {discount} lv.')