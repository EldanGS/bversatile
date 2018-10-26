"""
Solution.
Complexity analysis:
Time: O(logN) - always
Memory: O(1) - always
"""

class Solution:
	def power(self, x, y):
		result, power = 1.0, y
		if y < 0:
			power, x = -power, 1.0 / x

		while power:
			if power & 1:
				result *= x
			x, power = x * x, power >> 1

		return result
		
if __name__ == '__main__':
	x, y = 3.3, 7
	Solution = Solution()
	print(Solution.power(x, y))
