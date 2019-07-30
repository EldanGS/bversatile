"""
Given two strings S and T, determine if they are both one edit distance apart.

Example
Example 1:

Input: s = "aDb", t = "adb"
Output: true
Example 2:

Input: s = "ab", t = "ab"
Output: false
Explanation:
s=t ,so they aren't one edit distance apart
"""


def isOneEditDistance(s, t):
    n, m = len(s), len(t)
    if abs(n - m) > 1:
        return False

    i = j = diff = 0
    while i < n and j < m:
        if s[i] != t[j]:
            if diff == 1:
                return False

            if n > m:
                i += 1
            elif n < m:
                j += 1
            else:
                i, j = i + 1, j + 1
            diff += 1
        else:
            i, j = i + 1, j + 1

    diff += i < n or j < m

    return diff == 1


def __test(s, t, expected):
    actual = isOneEditDistance(s, t)

    assert actual == expected, 'Wrong answer'
    print('Accepted')


if __name__ == '__main__':
    s, t = "aDb", "adb"
    __test(s, t, True)

    s, t = "a", "adb"
    __test(s, t, False)

    s, t = "aDbb", "adb"
    __test(s, t, False)

    s, t = "Dab", "adb"
    __test(s, t, False)

    s, t = "adB", "adb"
    __test(s, t, True)