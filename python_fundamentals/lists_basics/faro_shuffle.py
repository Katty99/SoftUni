cards = input().split()
number_of_shuffles = int(input())
for current_shuffle in range(number_of_shuffles):
    shuffled_list = []
    middle = int(len(cards)) // 2
    lhs = cards[:middle]
    rhs = cards[middle::]
    for index in range(len(lhs)):
        shuffled_list.append(lhs[index])
        shuffled_list.append(rhs[index])
    cards = shuffled_list
print(cards)


