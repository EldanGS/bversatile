"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""

class Solution:
	def reverse(self, x):
		result, x_remaining = 0, abs(x)
		while x_remaining:
			result = result * 10 + (x_remaining % 10)
			x_remaining //= 10

		if x < 0:
			result = -result

		return result
		
if __name__ == '__main__':
	x = -314
	Solution = Solution()
	print(Solution.reverse(x))
