# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def isOneBitCharacter(self, bits):
        if not bits:
            return False
        
        n = len(bits)
        i = 0
        while i < n:
            if i == n - 1:
                return True
            if bits[i]:
                i += 2
            else:
                i += 1
        
        return False
