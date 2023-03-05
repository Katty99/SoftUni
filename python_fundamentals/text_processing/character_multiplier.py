sequence = input().split()
first = sequence[0]
second = sequence[1]
total_sum = 0
if len(first) == len(second):
    for index in range(len(first)):
        total_sum += ord(first[index]) * ord(second[index])
elif len(first) > len(second):
    for index in range(len(second)):
        total_sum += ord(first[index]) * ord(second[index])
    for index in range(len(second), len(first)):
        total_sum += ord(first[index])
else:
    for index in range(len(first)):
        total_sum += ord(first[index]) * ord(second[index])
    for index in range(len(first), len(second)):
        total_sum += ord(second[index])
print(total_sum)
