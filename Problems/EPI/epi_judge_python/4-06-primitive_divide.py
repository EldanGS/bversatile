from test_framework import generic_test


def divide(x, y):
    result, k = 0, 32
    power = y << k

    while x >= y:
        while power > x:
            power >>= 1
            k -= 1

        result += 1 << k
        x -= power

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("4-06-primitive_divide.py",
                                       "primitive_divide.tsv", divide))
