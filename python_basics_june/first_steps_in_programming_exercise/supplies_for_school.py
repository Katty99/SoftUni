pens = int(input())
markers = int(input())
detergent = int(input())
cost_of_pens = pens * 5.8
cost_of_markers = markers * 7.2
cost_of_detergent = detergent * 1.2
cost = cost_of_detergent + cost_of_markers + cost_of_pens
discount = int(input())
total_cost = cost - cost * discount / 100
print(total_cost)

