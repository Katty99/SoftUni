stay_days = int(input())
accommodation_type = input()
feedback = input()
price = 0

stay_nights = stay_days - 1

if accommodation_type == 'room for one person':
    price = 18
elif accommodation_type == 'apartment':
    price = 25
    if stay_days < 10:
        price *= 0.7
    elif 10 <= stay_days <= 15:
        price *= 0.65
    else:
        price *= 0.5
elif accommodation_type == 'president apartment':
    price = 35
    if stay_days < 10:
        price *= 0.9
    elif 10 <= stay_days <= 15:
        price *= 0.85
    else:
        price *= 0.8
total_sum = stay_nights * price
if feedback == 'positive':
    total_sum *= 1.25
elif feedback == 'negative':
    total_sum *= 0.9
print(f'{total_sum: .2f}')
