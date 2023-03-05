money = input().split(', ')
number_of_beggars = int(input())
money_to_int = []
total_list = []
starting_index = 0
for converted in money:
    money_to_int.append(int(converted))
while starting_index < number_of_beggars:
    money_per_beggar = 0
    for current_amount in range(starting_index, len(money_to_int), number_of_beggars):
        money_per_beggar += money_to_int[current_amount]
    total_list.append(money_per_beggar)
    starting_index += 1
print(total_list)