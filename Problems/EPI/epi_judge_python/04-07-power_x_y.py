from test_framework import generic_test


def power(x, y):
    result, power = 1.0, y
    if y < 0:
        x, power = 1 / x, -power

    while power:
        if power & 1:
            result *= x
        x *= x
        power >>= 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("04-07-power_x_y.py", 'power_x_y.tsv', power))
