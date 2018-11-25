"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def brackets_match(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        else:
            if not stack or stack.pop() != c:
                return False

    return not stack


if __name__ == '__main__':
    s = '([])[]({})'#'()[[]'
    if brackets_match(s):
        print('balanced')
    else:
        print('unbalanced')