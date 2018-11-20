"""
Solution.
Complexity analysis:
Time: O(1) - always
Memory: O(1) - always
"""


class Solution:
    def swap_bits(self, x, i, j):
        if (x >> i) & 1 != (x >> j) & 1:
            bitmask = (1 << i) | (1 << j)
            x ^= bitmask

        return x


if __name__ == '__main__':
    x = 11
    i = 2
    j = 0

    """
             3 2 1 0	
        11 = 1 0 1 1
        i = 2
        j = 0

        11 >> i = 11 >> 2 = 0010 = 2
        11 >> 0 = 11 >> 0 = 1011 = 11 
        last position of two shifted values is difference

        bitmask = (1 << i) | (1 << j) = (1 << 2) | (1 << 0) = 4 | 1 = 5 = 0101

        x 		= 11 = 1 0 1 1
        
        ^ (xor)
        
        bitmask = 5  = 0 1 0 1
        
        =
        
        x 		= 14 = 1 1 1 0
        
    """
    Solution = Solution()

    print(Solution.swap_bits(x, i, j))
