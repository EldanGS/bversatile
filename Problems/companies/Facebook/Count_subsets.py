# https://leetcode.com/discuss/interview-question/275785/Facebook-or-Phone-screen-or-Count-subsets

"""
Input:

Given an array A of
-positive
-sorted
-no duplicate
-integer

A positive integer k

Output:

Count of all such subsets of A,
Such that for any such subset S,
Min(S) + Max(S) = k
subset should contain at least two elements

Backtracking approach to get subsets
Get min and max of subset
Add min and max and put them in Hashmap (or update the count)
repeat this process for all subsets
search for k in hashmap and return count of k
input: {1,2,3,4,5}

subsets:
1, 2, 3, 4, 5, {1,2},{1,3}
k = 5

count = 5

{1, 4},{2,3} {1,2,4}, {1,2,3,4} {1,3,4}


For a given list of integers and integer K, find the number of non-empty subsets S such that min(S) + max(S) <= K.

Example 1:

nums = [2, 4, 5, 7]
k = 8
Output: 5
Explanation: [2], [4], [2, 4], [2, 4, 5], [2, 5]
Example 2:

nums = [1, 4, 3, 2]
k = 8
Output: 15
Explanation: 16 (2^4) - 1 (empty set) = 15
Example 3:

nums = [2, 4, 2, 5, 7]
k = 10
Output: 27
Explanation: 31 (2^5 - 1) - 4 ([7], [5, 7], [4, 5, 7], [4, 7]) = 27


Expected O(n^2) time solution or better.
"""


def count_subsets(nums, k):
    nums.sort()
    left, right, result = 0, len(nums) - 1, 0

    while left <= right:
        if nums[left] + nums[right] > k:
            right -= 1
        else:
            result += (1 << (right - left))
            left += 1

    return result


def _test(nums, k, expected):
    actual = count_subsets(nums, k)

    assert actual == expected, 'Wrong answer'
    print('Accepted')


if __name__ == '__main__':
    nums = [2, 4, 5, 7]
    k = 8
    _test(nums, k, 5)  # [2], [4], [2, 4], [2, 4, 5], [2, 5]

    nums = [2, 4, 2, 5, 7]
    k = 10
    _test(nums, k, 27)  # 31 (2^5 - 1) - 4 ([7], [5, 7], [4, 5, 7], [4, 7]) = 27
