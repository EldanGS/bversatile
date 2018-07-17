# https://leetcode.com/problems/jewels-and-stones/description/

"""
Solution, more concise
Complexity analysis:
Time: O(N)
Memory: O(const) 
"""
class Solution:
    def numJewelsInStones(self, J, S):
        return sum(map(J.count, S))
