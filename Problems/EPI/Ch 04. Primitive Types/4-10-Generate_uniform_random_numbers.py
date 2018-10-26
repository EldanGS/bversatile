"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""

class Solution:
	def uniform_random(self, lower_bound, upper_bound):
		number_of_outcomes = upper_bound - lower_bound + 1
		while True:
			result, i = 0, 0

			while (1 << i) < number_of_outcomes:
				# zero_one_random() is the provided random number
				result += (result << i) | zero_one_random()
				i += 1

			if result < number_of_outcomes:
				break

		return result + lower_bound