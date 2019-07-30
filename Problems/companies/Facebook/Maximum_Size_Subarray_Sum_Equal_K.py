"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:

Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

"""


def max_size_subarray_equal_k(nums, k):
    entity = {0: -1}
    result, prefix_sum = 0, 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum - k in entity:
            result = max(result, i - entity[prefix_sum - k])

        entity[prefix_sum] = i

    return result


def __test(nums, k, expected):
    actual = max_size_subarray_equal_k(nums, k)

    assert actual == expected, 'Wrong answer'
    print('Accepted')


if __name__ == '__main__':
    nums, k = [10, 5, 2, 7, 1, 9], 15
    __test(nums, k, 4)

    nums, k = [-5, 8, -14, 2, 4, 12], -5
    __test(nums, k, 5)
