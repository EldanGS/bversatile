"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def firstMissingPositive(numbers):
    n = len(numbers)
    for i in range(n):
        while (0 < numbers[i] <= n) and (numbers[i] != numbers[numbers[i] - 1]):
            numbers[numbers[i] - 1], numbers[i] = numbers[i], numbers[numbers[i] - 1]

    for i in range(n):
        if numbers[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == '__main__':
    numbers = [3, 4, -1, 1]  # [1, 2, 0]
    print(firstMissingPositive(numbers))
