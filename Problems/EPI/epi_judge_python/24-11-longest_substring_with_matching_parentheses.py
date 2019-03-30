from test_framework import generic_test


def longest_matching_parentheses(s):
    max_length, stack = 0, [-1]

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_length = max(max_length, i - stack[-1])
            else:
                stack.append(i)

    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "24-11-longest_substring_with_matching_parentheses.py",
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
