"""
Given a string str consisting of parentheses (, ) and alphanumeric characters.
Remove minimum number of paranthesis to make the string valid and return any valid result.
In a valid string for every opening/closing parentheses there is a matching closing/opening one.


Example 1:
Input: "ab(a(c)fg)9)"
Output: "ab(a(c)fg)9" or "ab(a(c)fg9)".

Example 2:
Input: ")a(b)c()("
Output: "a(b)c()"

Example 3:
Input: ")("
Output: ""

Example 4:
Input: "a(b))"
Output: "a(b)"

Example 5:
Input: "(a(c()b)"
Output: "(ac()b)" or "(a(c)b)"

Example 6:
Input: "(a)b(c)d(e)f)(g)"
Output: "(a)b(c)d(e)f(g)"

"""


def balance_parenthesis(s: str) -> str:
    if not s:
        return s

    remove = [False] * len(s)
    open = 0
    for i in range(len(s)):
        if s[i] == '(':
            open += 1
        elif s[i] == ')':
            if not open:
                remove[i] = True
            else:
                open -= 1

    close = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ')':
            close += 1
        elif s[i] == '(':
            if not close:
                remove[i] = True
            else:
                close -= 1

    result = ""
    for i in range(len(s)):
        if not remove[i]:
            result += s[i]

    return result


def __test(s, expected):
    actual = balance_parenthesis(s)
    assert actual == expected, 'Wrong answer, actual={}, expected={}'.format(actual, expected)
    print('Accept')


if __name__ == '__main__':
    s = "ab(a(c)fg)9)"
    __test(s, "ab(a(c)fg)9")

    s = ")a(b)c()("
    __test(s, "a(b)c()")

    s = ")("
    __test(s, "")

    s = "(a)b(c)d(e)f)(g)"
    __test(s, "(a)b(c)d(e)f(g)")
