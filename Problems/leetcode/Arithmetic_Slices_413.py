# https://leetcode.com/problems/arithmetic-slices/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - const
"""

class Solution:
    def numberOfArithmeticSlices(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        temp = 0
        
        for i in range(2, len(a)):
            if a[i - 1] - a[i - 2] == a[i] - a[i - 1]:
                temp += 1
                count += temp
            else:
                temp = 0
        
        return count
