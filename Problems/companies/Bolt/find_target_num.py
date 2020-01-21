"""
In an array of non-negative integers find a sequence of integers
which sum up to the given number. I.e. [1, 2, 3], find 5 -> return [2, 3]
"""


def find_sequence_sum_equals_to_target(nums: list, target: int) -> list:
    if not nums:
        return []

    n = len(nums)
    current_sum, left = nums[0], 0
    for right in range(1, n + 1):
        while left < right - 1 and current_sum > target:
            current_sum -= nums[left]
            left += 1
        if current_sum == target:
            return nums[left:right]

        if right < n:
            current_sum += nums[right]

    return []


def _test_find_sequence(nums, target, expected):
    actual = find_sequence_sum_equals_to_target(nums, target)
    assert actual == expected, 'Wrong answer: {} != {}'.format(expected, actual)
    print('Accepted')


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 5
    _test_find_sequence(nums, target, [2, 3])

    nums = [3, 4, 1, 2, 3]
    target = 6
    _test_find_sequence(nums, target, [1, 2, 3])

    nums = [0, 0, 2, 2, 5, 6, 7, 8, 9]
    target = 4
    _test_find_sequence(nums, target, [0, 0, 2, 2])

    nums = [0, 0, 1, 2, 3]
    target = 7
    _test_find_sequence(nums, target, [])
