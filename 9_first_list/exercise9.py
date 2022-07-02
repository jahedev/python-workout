def first_last(s):
    if len(s) < 2:
        return s
    return s[:1] + s[-1:]

if __name__ == '__main__':
    print(first_last(tuple('mubashir')))