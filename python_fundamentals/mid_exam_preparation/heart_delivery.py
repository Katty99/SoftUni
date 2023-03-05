number_of_hearts = [int(x) for x in input().split('@')]
current_position = 0
while True:
    command = input()
    if command == 'Love!':
        break
    else:
        command = command.split()
        length = int(command[1])
        if current_position + length >= len(number_of_hearts):
            length = 0
        else:
            length += current_position
        current_position = length
        if number_of_hearts[length] <= 0:
            print(f"Place {length} already had Valentine's day.")
        else:
            number_of_hearts[length] -= 2
            if number_of_hearts[length] <= 0:
                print(f"Place {length} has Valentine's day.")

print(f"Cupid's last position was {current_position}.")
failed_count = 0
for current_house in number_of_hearts:
    if current_house != 0:
        failed_count += 1
if failed_count == 0:
    print('Mission was successful.')
else:
    print(f"Cupid has failed {failed_count} places.")
