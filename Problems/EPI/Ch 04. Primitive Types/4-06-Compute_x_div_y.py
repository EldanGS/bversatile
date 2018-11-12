"""
Using only the addition, substraction, and shifting operators.

Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""


class Solution:
    def divide(self, x, y):
        result, power = 0, 32
        y_power = y << power
        while x >= y:
            while y_power > x:
                y_power >>= 1
                power -= 1

            result += 1 << power
            x -= y_power

        return result


if __name__ == '__main__':
    x, y = 80, 2
    Solution = Solution()
    print(Solution.divide(x, y))
