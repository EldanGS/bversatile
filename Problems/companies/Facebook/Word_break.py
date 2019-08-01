"""
Question 1:

Can you break the given string into words, provided by a given hashmap of frequency of word as <word: n>

Example 1:

HashMap -> {"abc":3, "ab":2, "abca":1}
String: "abcabcabcabca"
Output: true
Explanation: "abc" + "abc" + "abc" + "abca"
Example 2:

HashMap -> {"abc":3, "ab":2}
String: "abcabab"
Output: true
Explanation: "abc" + "ab" + "ab"
Example 3:

HashMap -> {"abc":3, "ab":2, "abca":1}
String: "abcx"
Output: false


"""


def can_break(data, s, start):
    if start == len(s):
        return True

    for end in range(start, len(s)):
        temp = s[start:end + 1]

        if data.get(temp, 0):
            data[temp] -= 1

            if can_break(data, s, end + 1):
                return True

            data[temp] += 1
    return False


def word_break(data, s):
    if not s:
        return True

    return can_break(data, s, 0)


def __test(data, s, expected):
    actual = word_break(data, s)

    assert actual == expected, 'Wrong answer'
    print('Accepted')


if __name__ == '__main__':
    data = {"abc": 3, "ab": 2, "abca": 1}
    s = 'abcabcabcabca'

    __test(data, s, True)


