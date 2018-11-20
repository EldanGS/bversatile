"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""


class Solution:
    def closest_int_same_bit_count(self, x):
        NUM_UNSIGNED_BITS = 64
        for i in range(NUM_UNSIGNED_BITS - 1):
            if (x >> i) & 1 != (x >> (i + 1)) & 1:
                x ^= (1 << i) | (1 << (i + 1))  # Swaps bit-i and bit-(i + 1)
                return x

        # Raise error if all bits of x are 0 or 1
        return ValueError('All bits are 0 or 1')


if __name__ == '__main__':
    x = 11
    """
      	weight is count of 1s bits
		x = 11 = 1011
		closest = 13 = 1101
    """

    Solution = Solution()

    print(Solution.closest_int_same_bit_count(x))
