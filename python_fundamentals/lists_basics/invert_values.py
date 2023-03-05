values = input().split()
inverted = []
for current_number in values:
    num_to_neg_int = -int(current_number)
    inverted.append(num_to_neg_int)
print(inverted)