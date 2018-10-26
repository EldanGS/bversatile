"""
Solution.
Complexity analysis:
Time: O(N^2) - always
Memory: O(1) - always
"""

class Solution:
	def multiply(self, x, y):
		def add(a, b):
			running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
			while temp_a or temp_b:
				ak, bk = a & k, b & k
				carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
				running_sum |= ak ^ bk ^ carryin
				carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)

			return running_sum | carryin

		running_sum = 0
		while x:
			if x & 1:
				running_sum = add(running_sum, y)
			x, y = x >> 1, y << 1

		return running_sum

if __name__ == '__main__':
	x, y = 5, 10
	Solution = Solution()
	print(Solution.multiply(x, y))