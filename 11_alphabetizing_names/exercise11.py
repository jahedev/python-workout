def alphabetize_names(p):
    return sorted(p, key=lambda person: [person['last'], person['first']])


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
    print(alphabetize_names(PEOPLE))
