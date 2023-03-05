number_of_inputs = int(input())
unfiltered_numbers = []
EVEN = 'even'
ODD = 'odd'
NEGATIVE = 'negative'
POSITIVE = 'positive'
for num in range(number_of_inputs):
    current_number = int(input())
    unfiltered_numbers.append(current_number)
command = input()
filtered_number = []
for number in unfiltered_numbers:
    filtered_passes =(
        (command == EVEN and number % 2 == 0) or
        (command == ODD and number % 2 != 0) or
        (command == NEGATIVE and number < 0) or
        (command == POSITIVE and number >= 0)
    )
    if filtered_passes:
        filtered_number.append(number)
print(filtered_number)