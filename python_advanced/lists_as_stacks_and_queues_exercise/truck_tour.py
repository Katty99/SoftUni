from collections import deque

number_of_petrol_pumps = int(input())
petrol_info_stack = deque([[int(x) for x in input().split()] for _ in range(number_of_petrol_pumps)])
petrol_info_stack_copy = petrol_info_stack.copy()
index = 0
petrol_in_tank = 0
while petrol_info_stack_copy:
    petrol, distance = petrol_info_stack_copy.popleft()
    petrol_in_tank += petrol
    if petrol_in_tank < distance:
        petrol_info_stack.rotate(-1)
        petrol_info_stack_copy = petrol_info_stack.copy()
        index += 1
        petrol_in_tank = 0
    else:
        petrol_in_tank -= distance
print(index)