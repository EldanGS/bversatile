# https://leetcode.com/problems/roman-to-integer/


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = roman[s[-1]]
        for i in reversed(range(len(s) - 1)):
            num += -roman[s[i]] if roman[s[i]] < roman[s[i + 1]] else roman[s[i]]

        return num
