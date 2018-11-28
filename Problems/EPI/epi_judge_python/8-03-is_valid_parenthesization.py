from test_framework import generic_test


def is_well_formed(s):
    stack, LOOKUP = [], {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in LOOKUP:
            stack.append(LOOKUP[c])
        elif not stack or stack.pop() != c:
            return False

    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("8-03-is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
