"""
1st solution.
Complexity analysis:
Time: O(longN) - in worst case
Memory: O(1) - always
"""

class Solution1:
	def computing_parity(self, x):
		result = 0
		while x > 0:
			result ^= x & 1
			x >>= 1

		return result


"""
2nd solution.
Complexity analysis:
Time: O(1) - always
Memory: O(1) - always
"""
class Solution2:
	def computing_parity(self, x):
		x ^= x >> 32
		x ^= x >> 16
		x ^= x >> 8
		x ^= x >> 4
		x ^= x >> 2
		x ^= x >> 1

		return x & 0x1

if __name__ == '__main__':

	solution1 = Solution1()
	solution2 = Solution2()
	for x in range(10):
		print('X is {}'.format(x))
		print('Computing the Parity of a Word, Solution 1: {}'.format(solution1.computing_parity(x)))
		print('Computing the Parity of a Word, Solution 2: {}\n'.format(solution2.computing_parity(x)))
	
	


