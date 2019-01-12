# https://leetcode.com/contest/weekly-contest-100/problems/monotonic-array/

"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(1) - always
"""
class Solution:
    def isMonotonic(self, a):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase, dicrease = 1, 1
        for i in range(1, len(a)):
            if a[i - 1] <= a[i]:
                increase += 1
            if a[i - 1] >= a[i]:
                dicrease += 1
        
        return (increase == len(a) or dicrease == len(a))