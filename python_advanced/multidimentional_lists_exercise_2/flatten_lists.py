matrix = [x.split() for x in input().split('|')]
print(*[' '.join(x) for x in matrix[::-1] if x])