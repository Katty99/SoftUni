first_result = input()
second_result = input()
third_result = input()
win_counter = 0
lose_counter = 0
drawn_counter = 0

if int(first_result[0]) > int(first_result[2]):
    win_counter += 1
elif int(first_result[0]) < int(first_result[2]):
    lose_counter += 1
else:
    drawn_counter += 1
if int(second_result[0]) > int(second_result[2]):
    win_counter += 1
elif int(second_result[0]) < int(second_result[2]):
    lose_counter += 1
else:
    drawn_counter += 1
if int(third_result[0]) > int(third_result[2]):
    win_counter += 1
elif int(third_result[0]) < int(third_result[2]):
    lose_counter += 1
else:
    drawn_counter += 1
print(f'Team won {win_counter} games.')
print(f'Team lost {lose_counter} games.')
print(f'Drawn games: {drawn_counter}')
