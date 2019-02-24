# https://leetcode.com/problems/expression-add-operators/


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(num, temp, curr, last):
            if not num:
                if curr == target:
                    result.append(temp)
                return

            for i in range(1, len(num) + 1):
                val = num[:i]

                if i == 1 or (i > 1 and num[0] != '0'):
                    dfs(num[i:], temp + '+' + val, curr + int(val), int(val))
                    dfs(num[i:], temp + '-' + val, curr - int(val), -int(val))
                    dfs(num[i:], temp + '*' + val, curr - last + last * int(val), last * int(val))

        result = []
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i]))

        return result
