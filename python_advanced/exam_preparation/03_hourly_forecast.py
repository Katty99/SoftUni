def forecast(*args):
    weather_info = {}
    for element in args:
        if element not in weather_info:
            weather_info[element[0]] = element[1]

    sunny = ''
    cloudy = ''
    rainy = ''

    for key, value in sorted(weather_info.items(), key=lambda x: x[0]):
        if value == 'Sunny':
            sunny += f"{key} - {value}\n"
        elif value == 'Cloudy':
            cloudy += f'{key} - {value}\n'
        elif value == 'Rainy':
            rainy += f'{key} - {value}\n'

    return sunny + cloudy + rainy


print(forecast(("Sofia", "Sunny"), ("London", "Cloudy"), ("New York", "Sunny")))
