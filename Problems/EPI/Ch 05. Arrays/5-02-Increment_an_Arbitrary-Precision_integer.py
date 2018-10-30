"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(1) - always
"""

def plus_One(A):
	A[-1] += 1

	for i in reversed(range(1, len(A))):
		if A[i] != 10:
			break
		A[i] = 0
		A[i - 1] += 1

	if A[0] == 10:
		A[0] = 1
		A.append(0)

	return A

if __name__ == '__main__':
	A = [9, 9]

	print(plus_One(A))