"""
Given a set of positive numbers, find the total number of subsets whose sum is
equal to a given number ‘S’.

Example 1: #
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.

Example 2: #
Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

"""


def count_subsets_rec(nums, i, target, memo):
    if target == 0:
        return 1
    elif i >= len(nums):
        return 0
    if memo[i][target] == -1:
        first_part = 0
        if nums[i] <= target:
            first_part = count_subsets_rec(nums, i + 1, target - nums[i], memo)

        second_part = count_subsets_rec(nums, i + 1, target, memo)
        memo[i][target] = first_part + second_part
    return memo[i][target]


def count_subsets(nums, target):
    memo = [[-1] * (target + 1) for _ in nums]
    return count_subsets_rec(nums, 0, target, memo)


def count_subsets_iter_dp(nums, target):
    dp = [[1] + [0] * target for _ in nums]

    for s in range(1, target + 1):
        dp[0][s] = nums[0] == s

    for i in range(1, len(nums)):
        for s in range(1, target + 1):
            dp[i][s] = dp[i - 1][s]
            if nums[i] <= s:
                dp[i][s] += dp[i - 1][s - nums[i]]

    return dp[-1][-1]


def count_subsets_optimal(nums, target):
    dp = [1] + [0] * target
    for s in range(1, target + 1):
        dp[s] = nums[0] == s

    for i in range(1, len(nums)):
        for s in range(target, -1, -1):
            if s >= nums[i]:
                dp[s] += dp[s - nums[i]]

    return dp[-1]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
    print("")
    print("Total number of subsets " + str(count_subsets_iter_dp([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_iter_dp([1, 2, 7, 1, 5], 9)))
    print("")
    print("Total number of subsets " + str(count_subsets_optimal([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_optimal([1, 2, 7, 1, 5], 9)))


main()
