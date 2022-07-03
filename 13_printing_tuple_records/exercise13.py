def alphabetize_names(p):
    return sorted(p, key=lambda person: [person['last'], person['first']])


def print_tuple_records(people):
    for person in people:
        print('{:<20}  {:<20}  {:<20}'.format(
            person['last'], person['first'], person['email']))


if __name__ == '__main__':
    PEOPLE = [
        {
            'first': 'Reuven',
            'last': 'Lerner',
            'email': 'reuven@lerner.co.il'
        },
        {
            'first': 'Donald',
            'last': 'Trump',
            'email': 'president@whitehouse.gov'
        },
        {
            'first': 'Vladimir',
            'last': 'Putin',
            'email': 'president@kremvax.ru'
        },
        {
            'first': 'Tarkov',
            'last': 'Putin',
            'email': 'tarkov@putin.com'
        }
    ]

    print_tuple_records(alphabetize_names(PEOPLE))
