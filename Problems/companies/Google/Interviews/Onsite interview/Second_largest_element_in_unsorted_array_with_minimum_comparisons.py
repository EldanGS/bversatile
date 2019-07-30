# https://cs.stackexchange.com/questions/83022/find-largest-and-second-largest-elements-of-the-array

"""
    1. Array of integers unsorted and unique values, find second largest number.
    2. Use minimum of comparison to get value, as soon as possible.
"""

import itertools

def second_maximum(A):
    n = len(A)
    A = list(A)

    if n == 2:
        if A[0] > A[1]:
            return (0, 1)
        else:
            return (1, 0)

    W = [0] * (n // 2)
    M = [0] * (n // 2)

    for i in range(n // 2):
        if A[i * 2] < A[i * 2 + 1]:
            A[i * 2], A[i * 2 + 1] = A[i * 2 + 1], A[i * 2]
            M[i] = 1

        W[i] = A[i * 2]

    (j, k) = second_maximum(W)
    j_swap, k_swap = M[j], M[k]
    j, k = j * 2, k * 2

    if A[j + 1] > A[k]:
        k = j + 1
        k_swap = 0 - j_swap

    return (j + j_swap, k + k_swap)


if __name__ == '__main__':
    # test cases
    arr = [1, 2, 4, 5, 7, 9, 10, 19]
    correct = 0
    total = 0
    for perm in itertools.permutations(arr):
        total = total + 1
        (p, l) = second_maximum(perm)
        larg = perm[p]
        sec = perm[l]

        if larg != 19 or sec != 10:
            print(perm)
        else:
            correct = correct + 1
            print("correct = {}/{}".format(correct, total))

    print(correct, total)