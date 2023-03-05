import os


def shopping_list(budget, **kwargs):
    products_bought = {}
    if budget >= 100:
        for product, info in kwargs.items():
            price = float(info[0])
            quantity = int(info[1])
            amount = price * quantity
            if budget - amount > 0 and len(products_bought) < 5:
                budget -= amount
                if product not in products_bought:
                    products_bought[product] = 0
                products_bought[product] += amount
    else:
        return "You do not have enough budget."

    result = []
    for key, value in products_bought.items():
        result.append(f"You bought {key} for {value:.2f} leva.")
    return os.linesep.join(result)


# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))