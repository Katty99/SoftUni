import os


def shopping_cart(*args):
    food_dictionary = {'Pizza': [], 'Soup': [], 'Dessert': []}
    to_print = []
    no_items = 0

    for current in args:
        if current == 'Stop':
            for key, value in sorted(food_dictionary.items(), key=lambda x: (-len(x[1]), x[0])):
                value = sorted(value)
                to_print.append(key + ':')
                if not value:
                    no_items += 1
                for val in value:
                    to_print.append(' - ' + val)
            if no_items == 3:
                return 'No products in the cart!'
            return os.linesep.join(to_print)

        food = current[0]
        ingredient = current[1]
        if food == 'Pizza':
            if food not in food_dictionary:
                food_dictionary[food] = []
            if len(food_dictionary[food]) == 4:
                continue
            if ingredient not in food_dictionary[food]:
                food_dictionary[food].append(ingredient)

        elif food == 'Soup':
            if food not in food_dictionary:
                food_dictionary[food] = []
            if len(food_dictionary[food]) == 3:
                continue
            if ingredient not in food_dictionary[food]:
                food_dictionary[food].append(ingredient)

        elif food == 'Dessert':
            if food not in food_dictionary:
                food_dictionary[food] = []
            if len(food_dictionary[food]) == 2:
                continue
            if ingredient not in food_dictionary[food]:
                food_dictionary[food].append(ingredient)


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
