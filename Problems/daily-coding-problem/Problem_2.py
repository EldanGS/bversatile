"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - always
"""


def multiply(A):
    n = len(A)
    result = [0] * n
    product = 1

    for i in range(n):
        result[i] = product
        product *= A[i]

    product = 1
    for i in reversed(range(n)):
        result[i] *= product
        product *= A[i]

    return result


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]

    print('Product of Array Except Self')
    print('Before: {}'.format(A))
    print('After: {}'.format(multiply(A)));
