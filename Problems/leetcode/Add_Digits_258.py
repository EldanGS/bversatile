# https://leetcode.com/problems/add-digits/description/

"""
1st solution, basic.
Complexity analysis:
Time: O(logN) - always
Memory: O(1) - in worst case
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            num = sum
        
        return num
        

"""
2nd solution, basic.
Complexity analysis:
Time: O(logN) - always
Memory: O(1) - in worst case
"""
class Solution:
    # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        return 9 if num % 9 == 0 else num % 9

