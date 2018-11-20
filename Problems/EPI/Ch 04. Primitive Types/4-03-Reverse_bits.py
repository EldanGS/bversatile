"""
1st solution.
Complexity analysis:
Time: O(logN) - always
Memory: O(1) - always
"""


class Solution:
    def reverse_bits(self, n):
        reverse = 0
        for _ in range(32):
            reverse = (reverse << 1) + (n & 1)
            n >>= 1

        return reverse


if __name__ == '__main__':
    x = 43261596
    Solution = Solution()

    print(Solution.reverse_bits(x))

    """
	Input: 43261596
	Output: 964176192
	Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.

    """
