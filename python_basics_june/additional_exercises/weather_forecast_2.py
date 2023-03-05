degrees = float(input())

if 26 <= degrees <= 35:
    print(f'Hot')
elif 20 < degrees < 26:
    print(f'Warm')
elif 15 <= degrees <= 20:
    print(f'Mild')
elif 12 <= degrees < 15:
    print(f'Cool')
elif 5 <= degrees < 12:
    print(f'Cold')
else:
    print(f'unknown')
