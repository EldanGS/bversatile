"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""


def decode_ways(s):
    if not len(s):
        return 0

    actual, prev = 1, 0
    n = len(s)
    for i in range(n):
        temp = 0
        if s[i] != '0':
            temp = actual
        if i > 0 and s[i - 1] != '0' and int(s[i - 1:i + 1]) < 27:
            temp += prev

        prev = actual
        actual = temp

    return actual


if __name__ == '__main__':
    print(decode_ways("123")) # ABC, LC, AX
