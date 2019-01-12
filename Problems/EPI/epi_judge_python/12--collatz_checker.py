from test_framework import generic_test


def test_collatz_conjecture(n):
    verified_numbers = set()
    for i in range(3, n + 1):
        sequence = set()
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                return False
            sequence.add(test_i)
            if test_i & 1:
                if test_i in verified_numbers:
                    break
                verified_numbers.add(test_i)
                test_i = 3 * test_i + 1
            else:
                test_i //= 2
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("12--collatz_checker.py",
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
