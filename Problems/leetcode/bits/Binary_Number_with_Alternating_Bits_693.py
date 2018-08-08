# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

"""
1st solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_bin = ''
        while n > 0:
            if n & 1:
                n_bin += '1'
            else:
                n_bin += '0'
            n >>= 1
        
        for i in range(len(n_bin) - 1):
            if (n_bin[i] == '1' and n_bin[i + 1] == '1') or (n_bin[i] == '0' and n_bin[i + 1] == '0'):
                return False
        
        return True


"""
2nd solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - always
"""

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return '00' not in bin(n) and '11' not in bin(n)


