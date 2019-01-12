# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))