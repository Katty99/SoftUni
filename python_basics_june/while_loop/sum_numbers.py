constant_number = int(input())
current_number = 0
while True:
    smaller_number = int(input())
    current_number += smaller_number
    if current_number >= constant_number:
        break
print(current_number)

