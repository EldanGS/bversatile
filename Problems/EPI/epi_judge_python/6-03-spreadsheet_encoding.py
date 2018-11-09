from test_framework import generic_test

import functools


def ss_decode_col_id(col):
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("6-03-spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
