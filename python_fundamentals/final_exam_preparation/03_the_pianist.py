number_of_pieces = int(input())
collection = []
for current_piece in range(number_of_pieces):
    piece, composer, key = input().split('|')
    info = [piece, composer, key]
    collection += info
while True:
    command = input()
    if command == 'Stop':
        break
    if 'Add' in command:
        add, piece, composer, key = command.split('|')
        if piece not in collection:
            info = [piece, composer, key]
            collection += info
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif 'Remove' in command:
        remove, piece = command.split('|')
        if piece not in collection:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            index = collection.index(piece)
            del collection[index:index + 3]
            print(f"Successfully removed {piece}!")
    elif 'ChangeKey' in command:
        change, piece, new_key = command.split('|')
        if piece not in collection:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            index = collection.index(piece)
            replace = index + 2
            collection[replace] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
for x in range(0, len(collection), 3):
    print(f"{collection[x]} -> Composer: {collection[x+1]}, Key: {collection[x+2]}")
