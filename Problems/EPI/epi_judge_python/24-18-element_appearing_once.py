from test_framework import generic_test


def find_element_appears_once(A):
    counts = [0] * 32
    for x in A:
        for i in range(32):
            counts[i] += x & 1
            x >>= 1

    def handle_negative(n):
        return n if n < 2**31 else n - 2**32

    result = sum(1 << i for i, c in enumerate(counts) if c % 3)

    return handle_negative(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("24-18-element_appearing_once.py",
                                       'element_appearing_once.tsv',
                                       find_element_appears_once))
