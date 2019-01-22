from test_framework import generic_test


def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("4-02-swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
