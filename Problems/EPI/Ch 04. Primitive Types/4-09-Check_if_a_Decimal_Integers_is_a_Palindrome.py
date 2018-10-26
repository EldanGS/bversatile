import math

"""
Solution.
Complexity analysis:
Time: O(logN) - in worst case
Memory: O(1) - always
"""

class Solution:
	def is_palindrome(self, x):
		if x <= 0:
			return x == 0

		num_digits = math.floor(math.log10(x)) + 1
		msd_mask = 10**(num_digits - 1)

		for i in range(num_digits // 2):
			if x // msd_mask != x % 10:
				return False

			x %= msd_mask
			x //= 10
			msd_mask //= 100

		return True

		
if __name__ == '__main__':
	x = 10201
	Solution = Solution()
	print('YES' if Solution.is_palindrome(x) else 'NO')

