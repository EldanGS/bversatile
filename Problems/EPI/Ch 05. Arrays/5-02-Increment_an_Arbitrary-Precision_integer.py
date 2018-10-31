from test_framework import generic_test

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
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_One))