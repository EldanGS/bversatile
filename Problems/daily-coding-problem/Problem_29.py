"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.

"""


def encode(s):
    if not s:
        raise ValueError('String is empty')

    result, count = '', 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1

    result += str(count) + s[-1]
    return result


if __name__ == '__main__':
    s = 'AAAABBBCCDAA'
    s = 'A'
    print(encode(s))
