width = int(input())
length = int(input())
initial_pieces = width * length
cake_size = width * length
piece_counter = 0

while cake_size >= 0:
    command = input()
    if command != 'STOP':
        number_of_pieces = int(command)
        cake_size -= number_of_pieces
        piece_counter += number_of_pieces
    else:
        break

difference = abs(piece_counter - initial_pieces)

if cake_size < 0:
    print(f'No more cake left! You need {difference} pieces more.')
else:
    print(f'{difference} pieces are left.')


