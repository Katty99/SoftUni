country_names = input().split(', ')
capital_cities = input().split(', ')
final = {country_names[i]: capital_cities[i] for i in range(len(capital_cities))}
for country, capital in final.items():
    print(f"{country} -> {capital}")
