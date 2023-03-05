from collections import deque

food_supplies = deque(int(x)for x in input().split(', '))
daily_stamina = deque(int(x) for x in input().split(', '))

NUMBER_OF_DAYS = 7
mountain_peaks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70
}
peak_index = 0
conquered_peaks = []

for day in range(NUMBER_OF_DAYS):
    if peak_index > 4:
        break
    current_sum = food_supplies.pop() + daily_stamina.popleft()
    current_peak = list(mountain_peaks.values())[peak_index]
    if current_sum >= current_peak:
        conquered_peaks.append(list(mountain_peaks.keys())[peak_index])
        peak_index += 1
    else:
        continue

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print('Conquered peaks:')
    print(*conquered_peaks, sep='\n')