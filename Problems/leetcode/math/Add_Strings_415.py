# https://leetcode.com/problems/add-strings/description/

"""
Solution.
Complexity analysis:
Time: O(N + M) - always
Memory: O(N + M) - in worst case
"""


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1) - 1, len(num2) - 1
        result = ""
        s = 0
        while s or n1 >= 0 or n2 >= 0:
            val1 = int(num1[n1]) if n1 >= 0 else 0
            val2 = int(num2[n2]) if n2 >= 0 else 0
            
            s = val1 + val2 + s
            result += str(s % 10)
            s = s // 10
            
            n1 -= 1
            n2 -= 1
        
        return "".join(result[::-1])
            
            