"""Given a set of positive numbers, partition the set into two subsets with
minimum difference between their subset sums.


Example 1: #
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

Example 2: #
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

Example 3: #
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
"""


def get_min_diff_partition(nums, i, set1_sum, set2_sum, memo):
    if i >= len(nums):
        return abs(set1_sum - set2_sum)
    if memo[i][set1_sum] == -1:
        diff1 = get_min_diff_partition(nums, i + 1, set1_sum + nums[i],
                                       set2_sum, memo)
        diff2 = get_min_diff_partition(nums, i + 1, set1_sum,
                                       set2_sum + nums[i], memo)
        memo[i][set1_sum] = min(diff1, diff2)

    return memo[i][set1_sum]


def min_diff_partition_rec_with_memo(nums):
    total = sum(nums)
    memo = [[-1] * (total + 1) for _ in nums]
    return get_min_diff_partition(nums, 0, 0, 0, memo)


def min_diff_partition(nums):
    total = sum(nums)
    target = (total // 2)
    dp = [[True] + [False] * target for _ in nums]

    for i in range(target + 1):
        dp[0][i] = nums[0] == i

    for i in range(1, len(nums)):
        for val in range(1, target + 1):
            if dp[i - 1][val]:
                dp[i][val] = dp[i - 1][val]
            elif val >= nums[i]:
                dp[i][val] = dp[i - 1][val - nums[i]]

    sum1 = 0
    for val in range(target, -1, -1):
        if dp[-1][val]:
            sum1 = val
            break
    sum2 = total - sum1
    return abs(sum2 - sum1)


def main():
    print(
        "Can partition: " + str(min_diff_partition_rec_with_memo([1, 2, 3, 9])))
    print("Can partition: " + str(
        min_diff_partition_rec_with_memo([1, 2, 7, 1, 5])))
    print("Can partition: " + str(
        min_diff_partition_rec_with_memo([1, 3, 100, 4])))

    print("")
    print("Can partition: " + str(min_diff_partition([1, 2, 3, 9])))
    print("Can partition: " + str(min_diff_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(min_diff_partition([1, 3, 100, 4])))


main()
