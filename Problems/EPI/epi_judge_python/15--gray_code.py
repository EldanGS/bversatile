import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def gray_code1(num_bits):
    def directed_gray_code(history):
        def differ_by_one_bit(x, y):
            bit_differ = x ^ y
            return bit_differ and not ((bit_differ - 1) & bit_differ)

        if len(result) == 1 << num_bits:
            return differ_by_one_bit(result[0], result[-1])

        for i in range(num_bits):
            previous_code = result[-1]
            candidate_next_code = previous_code ^ (1 << i)
            if candidate_next_code not in history:
                history.add(candidate_next_code)
                result.append(candidate_next_code)
                if directed_gray_code(history):
                    return True
        return False

    result = [0]
    directed_gray_code(set([0]))
    return result


def gray_code(num_bits):
    result = [0]
    for i in range(num_bits):
        result += [x + 2 ** i for x in reversed(result)]

    return result


@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    def differs_by_1_bit(a, b):
        x = a ^ b
        if x == 0:
            return False
        while x & 1 == 0:
            x >>= 1
        return x == 1

    result = executor.run(functools.partial(gray_code, num_bits))

    expected_size = (1 << num_bits)
    if len(result) != expected_size:
        raise TestFailure("Length mismatch: expected " + str(expected_size) +
                          ", got " + str(len(result)))
    for i in range(1, len(result)):
        if not differs_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure("Two adjacent entries are equal")
            else:
                raise TestFailure(
                    "Two adjacent entries differ by more than 1 bit")

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure("Not all entries are distinct: found " +
                          str(len(result) - len(uniq)) + " duplicates")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("15--gray_code.py", "gray_code.tsv",
                                       gray_code_wrapper))
