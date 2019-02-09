import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A):
    miss_XOR_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)
    differ_bit, miss_or_dup = miss_XOR_dup & (~(miss_XOR_dup - 1)), 0
    for i, a in enumerate(A):
        if differ_bit & i:
            miss_or_dup ^= i
        if differ_bit & a:
            miss_or_dup ^= a

    return (DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_XOR_dup) if miss_or_dup in A else
            DuplicateAndMissing(miss_or_dup ^ miss_XOR_dup, miss_or_dup))


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    # find_duplicate_missing([1, 0, 2, 3, 3])
    exit(
        generic_test.generic_test_main(
            "11-10-search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
