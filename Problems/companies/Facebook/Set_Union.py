"""
Description

There is a list composed by sets. If two sets have the same elements, merge them.
In the end, there are several sets left.

The number of sets n <= 1000.
The number of elements for each set m <= 100.
The element must be a non-negative integer and not greater than 100000.

Example

Example 1:
Input: list = [[1,2,3],[3,9,7],[4,5,10]]
Output: 2.
Explanation:There are 2 sets of [1,2,3,9,7] and [4,5,10] left.

Example 2:
Input:list = [[1],[1,2,3],[4],[8,7,4,5]]
Output: 2.
Explanation:There are 2 sets of [1,2,3] and [4,5,7,8] left.

"""


# O(N * M) time, where N is num of set, M length of each set
# O(M) space, where M is num of unique values
def set_union(list_of_set):
    if not list_of_set:
        return 0

    parents = {}
    for s in list_of_set:
        for num in s:
            parents[num] = num

    for s in list_of_set:
        if not s:
            continue

        p1 = find_parent(parents, s[0])
        for num in s[1:]:
            p2 = find_parent(parents, num)

            if p1 != p2:
                parents[p2] = p1

    return sum(parent == num for parent, num in parents.items())


def find_parent(parents, num):
    while parents[num] != num:
        parents[num] = parents[parents[num]]
        num = parents[num]

    return num


def _test(list_of_set, expected):
    actual = set_union(list_of_set)

    assert actual == expected, 'Wrong answer, actual: {}, expected: {}'.format(actual, expected)
    print('Accepted')


if __name__ == '__main__':
    list_of_set = [[1, 2, 3], [3, 9, 7], [4, 5, 10]]
    _test(list_of_set, 2)

    list_of_set = [[1], [1, 2, 3], [4], [8, 7, 4, 5]]
    _test(list_of_set, 2)

    list_of_set = [[], [1, 2, 3], [4], [8, 7, 4, 5]]
    _test(list_of_set, 2)