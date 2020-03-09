"""
countPairsWithSum
Given an array a of non-negative integers, find the
number of distinct pairs of integers for which the sum is equal to k.

Example
For k = 8 and a = [2, 3, 6, 2, 8],
the output should be  countPairsWithSum(k, a) = 1.
There are four pairs that sum up to 8: (a[0], a[2]), (a[2], a[0]), (a[2], a[3]),
and (a[3], a[2]), but all of them consist
of the same values 2 and 6, so there is only one unique pair.

"""
from collections import Counter


# O(N) time, O(N) space
def count_pair_with_sum1(a: list, k: int) -> int:
    if not a:
        return 0

    entity = Counter(a)
    pairs, count = {}, 0
    for i, num in enumerate(a):
        if k - num in entity:
            if (num, k - num) in pairs or (k - num, num) in pairs:
                continue

            pairs[(num, k - num)] = pairs[(k - num, num)] = 1
            count += 1

    return count


# O(NlogN) by time, O(1) space
def count_pair_with_sum2(a: list, k: int) -> int:
    if not a:
        return 0
    a.sort()
    left, right = 0, len(a) - 1
    pairs_count, left_pair, right_pair = 0, -1, -1
    while left < right:
        current_sum = a[left] + a[right]
        if current_sum > k:
            right -= 1
        elif current_sum < k:
            left += 1
        else:
            if a[left] != left_pair and a[right] != right_pair:
                pairs_count += 1
            left_pair, right_pair = a[left], a[right]
            left, right = left + 1, right - 1

    return pairs_count


def _test_count_pair_with_sum(a, k, expected):
    actual = count_pair_with_sum2(a, k)
    assert expected == actual, 'Wrong answer {} != {}'.format(expected, actual)
    print('Accepted')


if __name__ == '__main__':
    a = [2, 3, 6, 2, 6, 8]
    k = 8
    _test_count_pair_with_sum(a, k, 1)

    a = [2, 2]
    k = 4
    _test_count_pair_with_sum(a, k, 1)
