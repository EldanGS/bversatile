"""
In a binary matrix (all elements are 0 and 1), every row is sorted in ascending order (0 to the left of 1).
Find the leftmost column index with a 1 in it.

Example 1:

Input:
[[0, 0, 0, 1],
 [0, 0, 1, 1],
 [0, 1, 1, 1],
 [0, 0, 0, 0]]
Output: 1
Example 2:

Input:
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
Output: -1
Expected solution better than O(r * c).

"""


def leftmost_index(grid):
    if not grid or not grid[0]:
        return -1

    i, j = 0, len(grid[0]) - 1
    result = -1

    while i < len(grid) and j >= 0:
        if grid[i][j]:
            result = j
            j -= 1
        else:
            i += 1

    return result


def _test(grid, expected):
    actual = leftmost_index(grid)

    assert actual == expected, 'Wrong answer'
    print('Accepted')


if __name__ == '__main__':
    grid = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]]
    _test(grid, 1)

    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    _test(grid, -1)
