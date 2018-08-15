# https://leetcode.com/problems/max-chunks-to-make-sorted/description/

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def maxChunksToSorted(self, a):
        chunks, current = 0, 0
        n = len(a)
        
        for i in range(n):
            current = max(current, a[i])
            if current == i:
                chunks += 1
        
        return chunks
