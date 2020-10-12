# You have a dictionary of cities. Create dictionary of distances

from pprint import pprint
from math import sqrt

cities = {
    'Los Angeles': (550, 370),
    'Chicago': (510, 510),
    'Dallas': (480, 480)
}

distances = {}

los_angeles = cities['Los Angeles']
chicago = cities['Chicago']
dallas = cities['Dallas']

los_angeles_chicago = sqrt((chicago[0] - los_angeles[0]) ** 2 + (chicago[1] - los_angeles[1]) ** 2)
los_angeles_dallas = sqrt((dallas[0] - los_angeles[0]) ** 2 + (dallas[1] - los_angeles[1]) ** 2)
dallas_chicago = sqrt((dallas[0] - chicago[0]) ** 2 + (dallas[1] - chicago[1]) ** 2)

distances['Los Angeles'] = {}
distances['Los Angeles']['Chicago'] = los_angeles_chicago
distances['Los Angeles']['Dallas'] = los_angeles_dallas

distances['Chicago'] = {}
distances['Chicago']['Los Angeles'] = los_angeles_chicago
distances['Chicago']['Dallas'] = dallas_chicago

distances['Dallas'] = {}
distances['Dallas']['Los Angeles'] = los_angeles_dallas
distances['Dallas']['Chicago'] = dallas_chicago

pprint(distances)
