from test_framework import generic_test


def is_well_formed(s):
    data = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in s:
        if c in data:
            stack.append(data[c])
        elif not stack or stack.pop() != c:
                return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("08-03-is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
