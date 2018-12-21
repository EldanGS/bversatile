"""
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index
(we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""


def water_trap(A):
    left, right = 0, len(A) - 1
    result = 0
    max_left, max_right = 0, 0
    while left <= right:
        if A[left] <= A[right]:
            if max_left <= A[left]:
                max_left = A[left]
            else:
                result += max_left - A[left]
            left += 1
        else:
            if max_right <= A[right]:
                max_right = A[right]
            else:
                result += max_right - A[right]
            right -= 1

    return result


if __name__ == '__main__':
    A = [3, 0, 1, 3, 0, 5]
    # A = [2, 1, 2]

    print(water_trap(A))
