chicken = int(input())
fish = int(input())
vegetarian = int(input())
chicken_cost = chicken * 10.35
fish_cost = fish * 12.4
vegetarian_cost = vegetarian * 8.15
cost = chicken_cost + fish_cost + vegetarian_cost
dessert_cost = cost * 0.2
cost_of_delivery = 2.5
total_cost = cost + dessert_cost + cost_of_delivery
print(total_cost)
