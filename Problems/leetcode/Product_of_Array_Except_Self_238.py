# https://leetcode.com/problems/product-of-array-except-self/description/

"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""


# array  = [1, 2, 3, 4]
# front  = 1, 1, 2, 6
# back   = 24, 12, 4, 1
# result = 24, 12, 8, 6 => front[i] * back[i]
class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        n, product = len(nums), 1
        result = []
        for i in range(n):
            result.append(product)
            product *= nums[i]

        product = 1
        for i in reversed(range(n - 1)):
            product *= nums[i + 1]
            result[i] *= product

        return result
