"""
1st solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(1) - always
"""

def dutch_flag_partition(partition_index, A):
	pivot = A[partition_index]
	smaller = 0
	n = len(A)
	for i in range(n):
		if A[i] < pivot:
			A[i], A[smaller] = A[smaller], A[i]
			smaller += 1

	larger = n - 1
	for i in reversed(range(n)):
		if A[i] > pivot:
			A[i], A[larger] = A[larger], A[i]
			larger -= 1


"""
2nd solution, more concise 
Complexity analysis:
Time: O(N) - in worst case
Memory: O(1) - always
"""
def dutch_flag_partition2(partition_index, A):
	pivot = A[partition_index]
	smaller, equal, larger = 0, 0, len(A)

	while smaller < larger:
		if A[equal] < pivot:
			A[smaller], A[equal] = A[equal], A[smaller]
			smaller, equal = smaller + 1, equal + 1
		elif A[equal] == pivot:
			equal += 1
		else:
			larger -= 1
			A[equal], A[larger] = A[larger], A[equal]



if __name__ == '__main__':
	A = [0, 1, 2, 0, 2, 1, 1]
	partition_index = 3

	print('Array: {}, index: {}'.format(A, partition_index))
	dutch_flag_partition2(partition_index, A)
	print('Array: {}, index: {}'.format(A, partition_index))