from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:
            result.append(c * count)
            count = 0

    return ''.join(result)


def encoding(s):
    count, result = 1, []
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            result.append(str(count) + s[i - 1])
            count = 1
        else:
            count += 1

    return ''.join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("6-12-run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
