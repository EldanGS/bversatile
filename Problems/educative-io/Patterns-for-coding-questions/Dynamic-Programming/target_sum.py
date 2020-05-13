"""
You are given a set of positive numbers and a target sum ‘S’. Each number
should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways
to assign symbols to make the sum of the numbers equal to the target ‘S’.

Example 1: #
Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1':
                            {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

Example 2: #
Input: {1, 2, 7, 1}, S=9
Output: 2
Explanation: The given set has '2' ways to make a sum of '9':
                                        {+1+2+7-1} & {-1+2+7+1}

"""


# O(N * S) time & space complexity
def find_target_subsets(nums, s):
    total = sum(nums)
    if total < s or (total + s) % 2 != 0:
        return 0

    target = (s + total) // 2
    dp = [[1] + [0] * target for _ in nums]
    for val in range(1, target + 1):
        dp[0][val] = nums[0] == val

    for i in range(1, len(nums)):
        for val in range(1, target + 1):
            dp[i][val] = dp[i - 1][val]
            if nums[i] <= val:
                dp[i][val] += dp[i - 1][val - nums[i]]

    return dp[-1][-1]


def find_target_subsets_optimal(nums, s):
    total = sum(nums)
    if total < s or (total + s) % 2 != 0:
        return 0

    target = (s + total) // 2
    dp = [1] + [0] * target
    for val in range(1, target + 1):
        dp[val] = nums[0] == val

    for i in range(1, len(nums)):
        for val in range(target, -1, -1):
            if val >= nums[i]:
                dp[val] += dp[val - nums[i]]

    return dp[-1]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))
    print("")
    print("Total ways: " + str(find_target_subsets_optimal([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets_optimal([1, 2, 7, 1], 9)))

main()
