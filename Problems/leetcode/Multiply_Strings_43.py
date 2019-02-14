# https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)

        for i in reversed(range(n1)):
            for j in reversed(range(n2)):
                result[i + j + 1] += int(num1[i]) * int(num2[j])
                result[i + j] += result[i + j + 1] // 10
                result[i + j + 1] %= 10

        result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
        return ''.join(map(str, result))
