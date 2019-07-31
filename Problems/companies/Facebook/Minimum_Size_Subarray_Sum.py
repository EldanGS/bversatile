# https://www.lintcode.com/problem/minimum-size-subarray-sum/description

"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.


Example
Example 1:

Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: [1, 2, 3, 4, 5], s = 100
Output: -1
Challenge
If you have figured out the O(nlog n) solution, try coding another solution of which the time complexity is O(n).

"""


def minimumSize(nums, s):
    if not nums:
        return -1

    n, prefix_sum = len(nums), 0
    start, end = 0, 0
    result = float('inf')

    while end < n:
        prefix_sum += nums[end]

        while start <= end and prefix_sum >= s:
            result = min(result, end - start + 1)
            prefix_sum -= nums[start]
            start += 1

        end += 1

    return result if result != float('inf') else -1
