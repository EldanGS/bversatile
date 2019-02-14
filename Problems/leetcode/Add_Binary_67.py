# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        if not a and not b:
            return ''

        i, j = len(a) - 1, len(b) - 1
        result, rem = '', 0
        while i >= 0 or j >= 0 or rem == 1:
            rem += int(a[i]) if i >= 0 else 0
            rem += int(b[j]) if j >= 0 else 0

            result += str(rem & 1)
            rem >>= 1
            i, j = i - 1, j - 1

        return result[::-1]
