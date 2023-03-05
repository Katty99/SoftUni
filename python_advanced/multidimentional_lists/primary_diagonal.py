matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
total_sum = 0
for row in range(len(matrix)):
    total_sum += matrix[row][row]
print(total_sum)