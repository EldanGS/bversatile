"""
Given a 2D array of distinct integers with n numbers, "compress" the array such that the resulting array's numbers are in the range [1, n] and their relative order is kept.

Relative order means that if a number at position (row1, col1) is smaller than a number at position (row2, col2) in the original array, it should still have that relationship in the resulting array.

Example:
Input:
7 6
4 9

Output:
3 2
1 4

Followup:
Compress the array to make the numbers as small as possible as long as the relative order holds true for numbers in the same row and column.

Example1:
Input:
7 6
4 9

Output:
2 1
1 2

Example2:
Input:
25 74 54
12 56 83

Output:
2 4 3
1 2 4

Example3:
Input:
20 80 60 70
11 90 22 44
33 99 49 88

Output:
2 7 5 6
1 8 2 3
3 9 4 7

"""

import collections


# decorator for printing input and output
def test(func):
    def wrapper(A):
        print('input')
        for row in A: print(row)
        ans = func(A)
        print('output')
        for row in ans: print(row)
        print()
        return ans

    return wrapper


@test
def compress_2D_array(A):
    m, n = len(A), len(A[0])
    aux = sorted(
        ((r, c) for r in range(m) for c in range(n)),
        key=lambda p: A[p[0]][p[1]]
    )
    for v, (r, c) in enumerate(aux, 1): A[r][c] = v
    return A


@test
def compress_2D_array_followup(A):
    m, n = len(A), len(A[0])
    # Adjacency list of the directed graph
    G = collections.defaultdict(set)
    # For each node count the number of parent nodes
    cnt = {(r, c): 0 for r in range(m) for c in range(n)}

    # Sort each row, build graph and update counter
    for r, row in enumerate(A):
        order = sorted(range(n), key=lambda c: row[c])
        for c1, c2 in zip(order, order[1:]):
            G[(r, c1)].add((r, c2))
            cnt[(r, c2)] += 1

    # Sort each column, build graph and update counter
    for c, col in enumerate(zip(*A)):
        order = sorted(range(m), key=lambda r: col[r])
        for r1, r2 in zip(order, order[1:]):
            G[(r1, c)].add((r2, c))
            cnt[(r2, c)] += 1

    # Compress the matrix
    val = 1
    while cnt:
        # Find nodes that have no parent in the current graph
        peel = {k for k, v in cnt.items() if v == 0}
        # Modify matrix value at these nodes
        # Update the counter of their children
        # Then peel these nodes from the graph
        for r, c in peel:
            A[r][c] = val

            for ch in G[(r, c)]:
                cnt[ch] -= 1

            cnt.pop((r, c))

        val += 1
    return A


print('Initial Problem:')
A = [[7, 6], [4, 9]]
compress_2D_array(A)

print('Follow-up Problem:')
A = [[7, 6], [4, 9]]
compress_2D_array_followup(A)

A = [[25, 74, 54], [12, 56, 83]]
compress_2D_array_followup(A)

A = [[20, 80, 60, 70], [11, 90, 22, 44], [33, 99, 49, 88]]
compress_2D_array_followup(A)
