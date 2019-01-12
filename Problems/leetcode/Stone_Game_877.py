# https://leetcode.com/problems/stone-game/description/

"""
1st solution.
Complexity analysis:
Time: O(1) - always
Memory: O(1) - always
"""
class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True


"""
2nd solution, greedy algorithm.
Complexity analysis:
Time: O(NlogN) - in worst case
Memory: O(1) - always
"""
class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        piles.sort()
        
        alex, lee = 0, 0
        i = len(piles) - 1
        while i >= 0:
            alex += piles[i]
            lee += piles[i - 1]
            
            i -= 2
        
        return alex > lee

"""
3rd solution, dynamic programming.
Complexity analysis:
Time: O(N^2) - in worst case
Memory: O(N^2) - always
"""
class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0] * n for i in range(n)]
        
        for i in range(n):
            dp[i][i] = piles[i]
        
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])
        
        return dp[0][-1] > 0

"""
4th solution, dynamic programming.
Complexity analysis:
Time: O(N^2) - in worst case
Memory: O(N) - always
"""
class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = piles[:]
        
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + d] - dp[i])
        
        return dp[0] > 0