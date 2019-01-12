
"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""

class Solution:
    def findCelebrity(self, matrix):
    	n = len(matrix)
    	a, b = 0, n - 1

    	while a < b:
    		if matrix[a][b]:
    			a += 1
    		else:
    			b -= 1

    	for i in range(n):
    		if i != a and (matrix[a][i] or !matrix[i][a]):
    			return -1

    	return a