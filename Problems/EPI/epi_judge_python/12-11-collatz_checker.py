from test_framework import generic_test


def test_collatz_conjecture(n) -> bool:
    verified_number = set()
    for num in range(3, n + 1):
        sequence = set()
        test_num = num + 1
        while test_num >= num:
            if test_num in sequence:
                return False

            sequence.add(test_num)

            if test_num & 1:
                if test_num in verified_number:
                    break
                verified_number.add(test_num)
                test_num = test_num * 3 + 1
            else:
                test_num //= 2

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("12-11-collatz_checker.py",
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
