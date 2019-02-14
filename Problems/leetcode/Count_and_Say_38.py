# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        def directed_count_value(s):
            temp, count = '', 1
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    count += 1
                else:
                    temp += str(count) + s[i]
                    count = 1

            temp += str(count) + s[-1]
            return temp

        result = '1'
        for _ in range(n - 1):
            result = directed_count_value(result)

        return result
