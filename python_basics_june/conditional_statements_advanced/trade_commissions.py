city = input()
s = float(input())
commission = 0
error_condition = False

if city == 'Sofia':
    if 0 <= s <= 500:
        commission = s * 0.05
    elif 500 < s <= 1000:
        commission = s * 0.07
    elif 1000 < s <= 10000:
        commission = s * 0.08
    elif 10000 < s:
        commission = s * 0.12
    else:
        error_condition = True

elif city == 'Varna':
    if 0 <= s <= 500:
        commission = s * 0.045
    elif 500 < s <= 1000:
        commission = s * 0.075
    elif 1000 < s <= 10000:
        commission = s * 0.1
    elif 10000 < s:
        commission = s * 0.13
    else:
        error_condition = True
elif city == 'Plovdiv':
    if 0 <= s <= 500:
        commission = s * 0.055
    elif 500 < s <= 1000:
        commission = s * 0.08
    elif 1000 < s <= 10000:
        commission = s * 0.12
    elif 10000 < s:
        commission = s * 0.145
    else:
        error_condition = True
else:
    error_condition = True

if not error_condition:
    print(f'{commission:.2f}')
else:
    print('error')