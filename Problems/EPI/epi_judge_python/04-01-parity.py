from test_framework import generic_test


# O(logN) time, O(1) space
def parity1(x):
    counter = 0
    while x:
        counter ^= x & 1
        x >>= 1

    return counter


# O(1) time, O(1) space
def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1

    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("04-01-parity.py", 'parity.tsv', parity))
