def flights(*flights):
    flights_dictionary = {}
    for idx in range(0, len(flights), 2):
        flight = flights[idx]

        if flight == 'Finish':
            break

        passengers = flights[idx + 1]

        if flight not in flights_dictionary:
            flights_dictionary[flight] = 0

        flights_dictionary[flight] += int(passengers)
    return flights_dictionary


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))