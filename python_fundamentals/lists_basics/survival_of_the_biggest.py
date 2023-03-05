initial_numbers = input().split()
initial_list = []
for current_number in initial_numbers:
    initial_list.append(int(current_number))
number_of_removals = int(input())
for current_removal in range(number_of_removals):
    initial_list.remove(min(initial_list))
print(* initial_list, sep=', ')
