def add_first(numbers):
    for num in numbers:
        first_sequence.add(num)


def add_second(numbers):
    for num in numbers:
        second_sequence.add(num)


def remove_first(numbers):
    for num in numbers:
        if num in first_sequence:
            first_sequence.remove(num)


def remove_second(numbers):
    for num in numbers:
        if num in second_sequence:
            second_sequence.remove(num)


def check_subset(sequence1, sequence2):
    is_subset = False
    if sequence1.issubset(sequence2) or sequence2.issubset(sequence1):
        is_subset = True
    print(is_subset)


first_sequence = {int(x) for x in input().split()}
second_sequence = {int(x) for x in input().split()}
number_of_commands = int(input())

COMMAND_ADD_FIRST = 'Add First'
COMMAND_ADD_SECOND = 'Add Second'
COMMAND_REMOVE_FIRST = 'Remove First'
COMMAND_REMOVE_SECOND = 'Remove Second'

for current_command in range(number_of_commands):
    command = input()
    nums = [int(x) for x in command.split() if x.isdigit()]

    if command.startswith(COMMAND_ADD_FIRST):
        add_first(nums)

    elif command.startswith(COMMAND_ADD_SECOND):
        add_second(nums)

    elif command.startswith(COMMAND_REMOVE_FIRST):
        remove_first(nums)

    elif command.startswith(COMMAND_REMOVE_SECOND):
        remove_second(nums)

    else:
        check_subset(first_sequence, second_sequence)

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
