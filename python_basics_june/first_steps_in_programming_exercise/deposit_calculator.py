deposit = float(input())
months = int(input())
annual_interest = float(input())
monthly_interest = deposit * annual_interest / 12 / 100
overall_amount_paid = deposit + months * monthly_interest
print(overall_amount_paid)