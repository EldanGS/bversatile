from test_framework import generic_test

"""
1st solution.
Complexity analysis:
Time: O(longN) - in worst case
Memory: O(1) - always
"""

def parity1(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1

    return result

"""
2nd solution.
Complexity analysis:
Time: O(1) - always
Memory: O(1) - always
"""
def parity2(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1

    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("4-01-parity.py", 'parity.tsv', parity2))
