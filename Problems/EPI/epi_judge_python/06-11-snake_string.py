from test_framework import generic_test


def snake_string2(s):
    result = ''
    for i in range(1, len(s), 4):
        result += s[i]
    for i in range(0, len(s), 2):
        result += s[i]
    for i in range(3, len(s), 4):
        result += s[i]
    return result


def snake_string(s):
    return s[1::4] + s[::2] + s[3::4]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("06-11-snake_string.py", 'snake_string.tsv',
                                       snake_string))
