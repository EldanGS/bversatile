"""
If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate.
Give a count as well as print the strings.

For example:
Input: "1123". You need to general all valid alphabet codes from this string.

Output:

aabc //a = 1, a = 1, b = 2, c = 3
kbc // since k is 11, b = 2, c= 3
alc // a = 1, l = 12, c = 3
aaw // a= 1, a =1, w= 23
kw // k = 11, w = 23

"""


def decode_ways(s):
    if not s:
        return 0

    actual, prev = 1, 0
    for i in range(len(s)):
        temp = actual if s[i] != '0' else 0

        if i > 0 and s[i - 1] != '0' and '09' < s[i - 1:i + 1] < '27':
            temp += prev

        prev = actual
        actual = temp

    return actual

