nylon_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
working_hours = int(input())
nylon_cost = (nylon_quantity + 2) * 1.5
paint_cost = (paint_quantity * 14.5) + (paint_quantity * 0.1 * 14.5)
thinner_cost = thinner_quantity * 5
bags_cost = 0.4
cost_of_materials = nylon_cost + paint_cost + thinner_cost + bags_cost
labor_cost = working_hours * cost_of_materials * 0.3
total_cost = cost_of_materials + labor_cost
print(total_cost)
