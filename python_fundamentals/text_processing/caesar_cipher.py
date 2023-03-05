message = input()
encrypted = ''
for char in message:
    order = ord(char) + 3
    encrypted += chr(order)
print(encrypted)