# https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/


def can_partition(nums) -> bool:
    if not nums:
        return False

    total = sum(nums)
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum * 2 == total:
            print(nums[:i + 1], nums[i + 1:])
            return True

    return False


def __test(nums, expected):
    actual = can_partition(nums)

    assert actual == expected
    print('Accepted')


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 5]
    __test(nums, True)

    nums = [1, 3, 2]
    __test(nums, False)

    nums = [1, 2, 3]
    __test(nums, True)
