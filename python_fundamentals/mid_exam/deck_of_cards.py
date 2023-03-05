cards = input().split(', ')
num = int(input())
for current in range(1, num + 1):
    command = input().split(', ')
    action = command[0]

    if action == 'Add':
        card = command[1]
        if card not in cards:
            cards.append(card)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    elif action == 'Remove':
        card = command[1]
        if card in cards:
            cards.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif action == 'Remove At':
        index = int(command[1])
        if 0 <= index < len(cards):
            cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif action == 'Insert':
        index = int(command[1])
        card = command[2]
        if index < 0 or index >= len(cards):
            print("Index out of range")
        elif 0 <= index < len(cards) and card not in cards:
            cards.insert(index, card)
            print("Card successfully added")
        elif 0 <= index < len(cards) and card in cards:
            print("Card is already added")
print(', '.join(cards))