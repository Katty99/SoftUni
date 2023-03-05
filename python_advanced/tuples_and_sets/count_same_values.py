values = input().split()
counter = {}
for current in values:
    if current not in counter:
        counter[current] = 0
    counter[current] += 1
for k, v in counter.items():
    k = float(k)
    print(f"{k:.1f} - {v} times")