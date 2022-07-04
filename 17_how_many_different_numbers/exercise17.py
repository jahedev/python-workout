def how_many_different_numbers(arr):
    return len(set(arr))


if __name__ == '__main__':
    print(
        how_many_different_numbers([1, 2, 3, 1,
                                    2, 3, 4, 1]))
