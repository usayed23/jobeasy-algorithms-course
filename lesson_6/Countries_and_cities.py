# You have a list of countries and their cities. After that a list of cities is input.
# For every city indicate what country it is in.

# Input
# [
#   ['USA', 'Dallas', 'Washington', 'Los-Angeles', 'San-Francisco'],
#   ['Canada', 'Ottawa', 'Vancouver', 'Montreal']
# ]
# ['Montreal', 'Washington', 'Dallas']


# Output
# ['Canada', 'USA', 'USA']


def countries_and_cities(data, needed_cities):
    cities = {}
    result = []
    for item in data:
        for city in item[1:]:
            cities[city] = item[0]
    for city in needed_cities:
        if city in cities:
            result.append(cities[city])
    return result


print(countries_and_cities([
   ['USA', 'Dallas', 'Washington', 'Los-Angeles', 'San-Francisco'],
   ['Canada', 'Ottawa', 'Vancouver', 'Montreal'],
], ['Montreal', 'Washington', 'Dallas'])
)