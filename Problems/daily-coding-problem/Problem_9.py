"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13,
since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def largest_sum(A):
    if not A:
        return 0

    include, exclude = A[0], 0
    for a in A[1:]:
        temp = max(include, exclude)
        include = exclude + a
        exclude = temp

    return max(include, exclude)


if __name__ == '__main__':
    A = [2, 4, 6, 2, 5]  # [5, 1, 1, 5]
    print(largest_sum(A))
