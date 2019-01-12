# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

"""
Solution.
Complexity analysis:
Time: O(N) - ?
Memory: O(N) - in worst case
"""

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        data = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        primes = 0
        for value in range(L, R + 1):
            if bin(value).count('1') in data:
                primes += 1
        
        return primes