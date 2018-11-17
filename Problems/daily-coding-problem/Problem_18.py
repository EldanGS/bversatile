"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.

"""

from collections import deque


def max_values_subarray(A, k):
    dq = deque()
    n, result = len(A), []

    for i in range(k):
        while dq and A[i] >= A[dq[-1]]:
            dq.pop()
        dq.append(i)

    for i in range(k, n):
        result.append(A[dq[0]])

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and A[i] >= A[dq[-1]]:
            dq.pop()

        dq.append(i)

    result.append(A[dq[0]])
    return result


if __name__ == '__main__':
    A = [10, 2, 5, 7, 8, 7]
    k = 3

    print(max_values_subarray(A, k))
