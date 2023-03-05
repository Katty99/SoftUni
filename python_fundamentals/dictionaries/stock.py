bakery = input().split()
products_searched = input().split()
final = {}
for x in range(0, len(bakery), 2):
    key = bakery[x]
    value = bakery[x + 1]
    final[key] = int(value)

for current_product in products_searched:
    if current_product in final.keys():
        quantity = final[current_product]
        print(f"We have {quantity} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
