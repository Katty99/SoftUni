days_of_plunder = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())
total = 0
for current_day in range(1, days_of_plunder + 1):
    total += plunder_per_day
    if current_day % 3 == 0:
        total += plunder_per_day * 0.5
    if current_day % 5 == 0:
        total -= total * 0.3
if total >= expected_plunder:
    print(f'Ahoy! {total:.2f} plunder gained.')
else:
    print(f'Collected only {total * 100 / expected_plunder:.2f}% of the plunder.')