ranges_count = int(input())
max_length = 0
longest_intersection = set()
for x in range(ranges_count):
    first_intersection, second_intersection = input().split('-')
    first = [int(y) for y in first_intersection.split(',')]
    second = [int(y) for y in second_intersection.split(',')]
    first_range = {int(z) for z in range(first[0], first[1] + 1)}
    second_range = {int(z) for z in range(second[0], second[1] + 1)}
    current_intersection = first_range.intersection(second_range)
    if len(current_intersection) > max_length:
        max_length = len(current_intersection)
        longest_intersection = current_intersection
print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {max_length}")