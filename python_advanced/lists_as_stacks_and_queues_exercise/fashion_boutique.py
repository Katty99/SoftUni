clothes = [int(n) for n in input().split()]
rack_capacity = int(input())
sum_per_rack = 0
total_racks = 1
while clothes:
    current = clothes.pop()
    if sum_per_rack + current <= rack_capacity:
        sum_per_rack += current
    else:
        sum_per_rack = 0
        sum_per_rack += current
        total_racks += 1
print(total_racks)