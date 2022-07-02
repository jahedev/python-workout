"""
This challenge asks you to redefine the mysum function we defined in chapter 1, such that it can take any number of arguments. The arguments must all be of the same type and know how to respond to the + operator. (Thus, the function should work with numbers, strings, lists, and tuples, but not with sets and dicts.)
"""

def mysum(*args):
  if not args: return args
  elif type(args[0]) not in {int, float, str, list, tuple}:
      raise TypeError('All arguments must be of the same type.')

  sum = type(args[0])()
  for arg in args:
      sum += arg

  return sum

if __name__ == '__main__':
    print(mysum(1, 2, 3, 4))
    print(mysum(1.1, 2,2, 3.3, 4.4))
    print(mysum('a', 'b', 'c', 'd'))
    print(mysum([1, 2, 3, 4], [5, 6, 7, 8]))
    print(mysum((1, 2, 3, 4), (5, 6, 7, 8)))