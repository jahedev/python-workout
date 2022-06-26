"""
Write a program that simulates the sum function in python, except
that it takes any number of arguments, including ints, lists, and tuples.
"""

def num_sum(*nums):
    sum = 0
    for obj in nums:
        if type(obj) is list or type(obj) is tuple:
            for num in obj:
                sum += num
        else: sum += obj

    return sum

if __name__ == '__main__':
    print('ints 1-4: ', num_sum(1, 2, 3, 4))
    print('tuples 5-7: ', num_sum((5, 6, 7)))
    print('lists 8-10: ', num_sum([8, 9, 10]))
    print('ints, lists, tuples 1-10: ', num_sum(1, 2, 3, 4, [5, 6, 7], (8, 9, 10)))