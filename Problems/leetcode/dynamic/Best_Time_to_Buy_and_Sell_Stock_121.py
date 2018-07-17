# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

"""
Solution.
Complexity analysis:
Time: O(N)
Memory: O(1) - always
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy = float('inf')
        
        for price in prices:
            buy = min(buy, price)
            max_profit = max(max_profit, price - buy)
            
        return max_profit