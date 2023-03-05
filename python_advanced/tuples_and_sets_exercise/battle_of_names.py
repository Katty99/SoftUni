number_of_names = int(input())
odd_set = set()
even_set = set()
for x in range(1, number_of_names + 1):
    name = list(input())
    current_sum = 0
    for letter in name:
        current_sum += ord(letter)
    total_sum = int(current_sum / x)
    if total_sum % 2 == 0:
        even_set.add(total_sum)
    else:
        odd_set.add(total_sum)
odd_sum = sum(odd_set)
even_sum = sum(even_set)
if odd_sum == even_sum:
    print(*odd_set.union(even_set), sep=', ')
elif odd_sum > even_sum:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')

