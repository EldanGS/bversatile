"""
https://leetcode.com/discuss/interview-question/302028/LinkedIn-or-Smallest-K-Products-of-Two-Sorted-Array

Given two sorted integer arrays, find the smallest k products of the two arrays.

Example 1:

Input: arr1 = [-2, -1, 0, 1, 2], arr2 = [-3, -1, 2, 4, 5], k = 3
Output: [-10, -8, -6]
Explanation: -2 * 5, -2 * 4, 2 * -3

"""

import heapq


def separate_to_pos_n_neg(arr):
    pos, neg = [], []
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
    return pos, neg


def update_heap(a, b, i, j, d2, type, min_heap):
    if d2 == 1 and j < len(b):
        heapq.heappush(min_heap, (a[i] * b[j], i, j, d2, type))
    if d2 == -1 and -j <= len(b):
        heapq.heappush(min_heap, (a[i] * b[j], i, j, d2, type))


def push_k_elements(k, l1, l2, d1, d2, type, min_heap):
    if not l2:
        return None
    n = min(k, len(l1))
    x = 0 if d1 == 1 else -1
    y = 0 if d2 == 1 else -1
    for i in range(n):
        heapq.heappush(min_heap,(l1[x + d1 * i] * l2[y], x + d1 * i, y, d2, type))


def k_smallest_product(arr1, arr2, k):
    if not arr1 or not arr2 or not k:
        return []

    pos1, neg1 = separate_to_pos_n_neg(arr1)
    pos2, neg2 = separate_to_pos_n_neg(arr2)
    min_heap = []
    push_k_elements(k, pos1, pos2, 1, 1, 0, min_heap)
    push_k_elements(k, pos1, neg2, -1, 1, 1, min_heap)
    push_k_elements(k, neg1, pos2, 1, -1, 2, min_heap)
    push_k_elements(k, neg1, neg2, -1, -1, 3, min_heap)

    result = []
    while k > 0 and min_heap:
        k -= 1
        val, i, j, d2, type = heapq.heappop(min_heap)
        result.append(val)

        if type == 0:
            update_heap(pos1, pos2, i, j + d2, d2, type, min_heap)
        if type == 1:
            update_heap(pos1, neg2, i, j + d2, d2, type, min_heap)
        if type == 2:
            update_heap(neg1, pos2, i, j + d2, d2, type, min_heap)
        if type == 3:
            update_heap(neg1, neg2, i, j + d2, d2, type, min_heap)

    return result


print(k_smallest_product(arr1=[-2, -1, 0, 1, 2], arr2=[-3, -1, 2, 4, 5], k=25))
