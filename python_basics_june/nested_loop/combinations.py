result = int(input())
combinations = 0
for x1 in range(result + 1):
    for x2 in range(result + 1):
        for x3 in range(result + 1):
            if x1 + x2 + x3 == result:
                combinations += 1
print(combinations)
