easter_gifts = input().split()
command = input()
while command != "No Money":
    input_gift_list = command.split()
    if "OutOfStock" in input_gift_list:
        for index, value in enumerate(easter_gifts):
            if value == input_gift_list[1]:
                easter_gifts[index] = "None"
    elif "Required" in input_gift_list:
        replacing_index = int(input_gift_list[2])
        if replacing_index >= len(easter_gifts) or replacing_index < 0:
            command = input()
            continue
        easter_gifts[replacing_index] = input_gift_list[1]
    elif "JustInCase" in input_gift_list:
        easter_gifts[-1] = input_gift_list[1]
    command = input()
while "None" in easter_gifts:
    for index, value in enumerate(easter_gifts):
        if value == "None":
            easter_gifts.remove(easter_gifts[index])
print(*easter_gifts)