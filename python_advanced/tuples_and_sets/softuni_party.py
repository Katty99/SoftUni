number_of_guests = int(input())
reservation_numbers = set(input() for n in range(number_of_guests))
while True:
    guest_command = input()
    if guest_command == 'END':
        print(len(reservation_numbers))
        for current in sorted(reservation_numbers):
            print(current)
        break
    reservation_numbers.remove(guest_command)
