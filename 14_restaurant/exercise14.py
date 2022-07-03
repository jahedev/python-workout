"""
In this exercise, I want you to create a new constant dict, called MENU, representing the possible items you can order at a restaurant. The keys will be strings, and the val- ues will be prices (i.e., integers). You should then write a function, restaurant, that asks the user to enter an order:
 If the user enters the name of a dish on the menu, the program prints the price and the running total. It then asks the user again for their order.
 If the user enters the name of a dish not on the menu, the program scolds the user (mildly). It then asks the user again for their order.
 If the user enters an empty string, the program stops prompting and prints the total amount.
"""

import sys

MENU = {
    "sandwich": 10,
    "salad": 5,
    "chicken": 12,
    "tea": 7,
    "coffee": 8
}


def menu():
    total = 0

    print('What would you like to order? (Type `exit` to quit)')
    while (order := input('Order: ')) != 'exit':
        if order.lower() not in MENU:
            print(f'Sorry, we are fresh out of {order} today.')
            continue

        total += MENU[order]

        print('{} costs {}, total is {}'
              .format(order, MENU[order], total))

    print('\nYour total is: {}'.format(total))


if __name__ == '__main__':
    menu()
