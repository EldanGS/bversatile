# https://leetcode.com/problems/counting-bits/description/

"""
1st solution.
Complexity analysis:
Time: O(N) - ?
Memory: O(N) - always
"""
class Solution:
    def countBits(self, num):
        answer = []
        for n in range(num + 1):
            answer.append(bin(n).count('1'))
            
        return answer

"""
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

"""
2nd solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - always
"""
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if not num:
            return [0]
        dp = [0] * (num + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, num + 1):
            dp[i] = dp[i & 1] + dp[i // 2]
            
        return dp

"""
3rd solution, more concise.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - always
"""
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        
        return dp
    

