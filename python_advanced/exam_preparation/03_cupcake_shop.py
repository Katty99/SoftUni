def stock_availability(inventory, *args):
    if args[0] == 'delivery':
        for x in range(1, len(args)):
            inventory.append(args[x])
    elif args[0] == 'sell':
        if len(args) == 1:
            inventory.pop(0)
        elif str(args[1]).isnumeric():
            num = int(args[1])
            for x in range(num):
                inventory.pop(0)
        else:
            for y in range(1, len(args)):
                searched = args[y]
                inventory = [i for i in inventory if i != searched]
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))