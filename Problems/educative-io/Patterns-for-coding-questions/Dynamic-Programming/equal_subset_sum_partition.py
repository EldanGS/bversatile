"""Given a set of positive numbers, find if we can partition it into two
subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

Example 2:
Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}

Example 3:
Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.
"""


# O(2^n) time, O(N) space
def can_partition_recursive(nums, i, target):
    if target == 0:
        return True
    elif target < 0 or i >= len(nums):
        return False

    if nums[i] <= target:
        if can_partition_recursive(nums, i + 1, target - nums[i]):
            return True

    return can_partition_recursive(nums, i + 1, target)


# O(N * C) time, O(C) space, C is total sum
def can_partition_recursive_with_memo(nums, i, target, memo):
    if target == 0:
        return True
    elif target < 0 or i >= len(nums):
        return False

    if memo[i][target] != -1:
        return memo[i][target]

    if nums[i] <= target:
        if can_partition_recursive_with_memo(nums, i + 1, target - nums[i],
                                             memo):
            memo[i][target] = True
            return memo[i][target]

    memo[i][target] = can_partition_recursive_with_memo(nums, i + 1, target, memo)
    return memo[i][target]


# O(N * C) time, O(C) space, C is total sum
def can_partition_dp(nums, target):
    table = [True] + [False] * target
    for i, num in enumerate(nums):
        for part in range(target + 1):
            if num <= part:
                table[part] |= table[part - num]
    return table[-1]


def can_partition_naive(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2

    return can_partition_recursive(nums, 0, target)


def can_partition_with_memo(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2

    memo = [[-1] * (target + 1) for _ in nums]
    return can_partition_recursive_with_memo(nums, 0, target, memo)


def can_partition_iter_dp(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2

    return can_partition_dp(nums, target)


def main():
    print("Can partition: " + str(can_partition_naive([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition_naive([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_naive([2, 3, 4, 6])))
    print("")
    print("Can partition: " + str(can_partition_with_memo([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition_with_memo([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_with_memo([2, 3, 4, 6])))
    print("")
    print("Can partition: " + str(can_partition_iter_dp([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition_iter_dp([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_iter_dp([2, 3, 4, 6])))


main()
