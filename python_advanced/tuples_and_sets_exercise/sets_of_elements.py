n, m = [int(x) for x in input().split()]
set_n = {int(input()) for _ in range(n)}
set_m = {int(input()) for _ in range(m)}
intersection = set_n.intersection(set_m)
for num in intersection:
    print(num)