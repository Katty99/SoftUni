import re
destinations = input()
countries = []
travel_points = 0
pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
matches = re.findall(pattern, destinations)
for current in matches:
    countries.append(current[1])
for country in countries:
    travel_points += len(country)

print(f"Destinations: {', '.join(countries)}")
print(f"Travel Points: {travel_points}")
