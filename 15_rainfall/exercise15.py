"""
Specifically, write a function, get_rainfall, that tracks rainfall in a number of cit- ies. Users of your program will enter the name of a city; if the city name is blank, then the function prints a report (which I’ll describe) before exiting.
If the city name isn’t blank, then the program should also ask the user how much rain has fallen in that city (typically measured in millimeters). After the user enters the quantity of rain, the program again asks them for a city name, rainfall amount, and so on—until the user presses Enter instead of typing the name of a city.
When the user enters a blank city name, the program exits—but first, it reports how much total rainfall there was in each city. Thus, if I enter
"""

import sys

cities = {}


def validate_tokens(tokens):
    if len(tokens) < 2:
        return (False, 'requires two inputs separated by comma, a city name and rainfall amount')
    elif not tokens[-1].strip().isdigit():
        return (False, 'final input must be rainfall amount as an integer')
    return (True, 'Success')


def rainfall_print(city_name, amount):
    print('{:<15}  {:>10}'.format(city_name, amount))


def rainfall():
    print('Rainfall Tracker (type nothing to quit)')
    print('=====================================')
    while (user_input := input('city name + amount: ')) != '':
        tokens = [token.strip() for token in user_input.split()]

        valid = validate_tokens(tokens)
        if not valid[0]:
            print('Error: {}'.format(valid[1]))
            continue

        city_name = ' '.join(tokens[:-1]).strip().lower()
        amount = int(tokens[-1].strip())

        cities[city_name] = cities.get(city_name, 0) + amount

    print()
    if not cities:
        sys.exit()

    rainfall_print('City Name', 'Amount')

    for city_name, amount in cities.items():
        rainfall_print(city_name, amount)


if __name__ == '__main__':
    rainfall()
