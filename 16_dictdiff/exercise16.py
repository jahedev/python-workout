"""
Write a function, 
dictdiff, that takes two dicts as arguments. The function returns a 
new dict that expresses the difference between the two dicts.
"""


def dictdiff(dict1, dict2):
    output = {}

    for k, v in dict1.items():
        if v != dict2.get(k):
            output[k] = [v, dict2.get(k)]

    for k, v in dict2.items():
        if k not in output and v != dict1.get(k):
            output[k] = [dict1.get(k), v]

    return output


if __name__ == '__main__':
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}
    d3 = {'a': 1, 'b': 2, 'd': 3}
    d4 = {'a': 1, 'b': 2, 'c': 4}
    d5 = {'a': 1, 'b': 2, 'd': 4}

    print(dictdiff(d1, d1))
    print(dictdiff(d1, d2))
    print(dictdiff(d3, d4))
    print(dictdiff(d1, d5))
