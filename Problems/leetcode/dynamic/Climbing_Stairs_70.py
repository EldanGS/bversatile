# https://leetcode.com/problems/climbing-stairs/description/

"""
1st solution.
Complexity analysis:
Time: O(N)
Memory: O(N) 
"""
class Solution:
    def climbStairs(self, n):
        if n <= 1:
            return n
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1]

"""
2nd solution, memory optimize
Complexity analysis:
Time: O(N)
Memory: O(1) 
"""
class Solution:
    def climbStairs(self, n):
        if n <= 1:
            return n
        
        first = 1
        second = 2
        step = 2
        for i in range(2, n):
            step = first + second
            first = second
            second = step
        
        return step
