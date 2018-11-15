from test_framework import generic_test


def snake_string(s):
    return s[1::4] + s[::2] + s[3::4]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("6-11-snake_string.py", 'snake_string.tsv',
                                       snake_string))
