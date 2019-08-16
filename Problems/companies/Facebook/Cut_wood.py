# https://leetcode.com/discuss/interview-question/354854/Facebook-or-Phone-Screen-or-Cut-Wood

"""
Given an int array wood representing the length of n pieces of wood and an int k.
It is required to cut these pieces of wood such that more or equal to k pieces of the same length len are cut.
What is the longest len you can get?

Example 1:
Input: wood = [5, 9, 7], k = 3
Output: 5
Explanation:
5 -> 5
9 -> 5 + 4
7 -> 5 + 2

Example 2:
Input: wood = [5, 9, 7], k = 4
Output: 4
Explanation:
5 -> 4 + 1
9 -> 4 * 2 + 1
7 -> 4 + 3

"""


def can_partion(wood, K, part) -> bool:
    return sum((w - 1) // part for w in wood) <= K


def cut_wood(wood, K) -> int:
    if not wood:
        return -1

    left, right = 1, max(wood)
    while left <= right:
        mid = (left + right) // 2

        if can_partion(wood, K, mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


def _test(wood, K, expected):
    actual = cut_wood(wood, K)

    assert actual == expected, 'Wrong answer: {}'.format(actual)
    print('Accepted')


if __name__ == '__main__':
    wood, K = [5, 9, 7], 3
    _test(wood, K, 5)

    wood, K = [5, 9, 7], 4
    _test(wood, K, 4)
