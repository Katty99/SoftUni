def shop_from_grocery_list(budget, shopping_list, *products):
    for current in products:
        product = current[0]
        price = current[1]
        if product not in shopping_list:
            continue

        if budget - price >= 0:
            budget -= price
            shopping_list.remove(product)
        else:
            break

    if shopping_list:
        return f"You did not buy all the products. Missing products: {', '.join(shopping_list)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))