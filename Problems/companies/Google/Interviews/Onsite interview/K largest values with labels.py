"""
https://leetcode.com/discuss/interview-question/306851/Google-onsite-K-largest-values-with-labels

Given an array of values and their corresponding labels. Find out the k largest values, but each label cannot be used more than m times.

Example 1:

Input: values = [9, 8, 6, 8, 7], labels = [A, A, B, A, B], k = 3, m = 2
Output: [9, 8, 7]
Explanation: 8 > 7, but we can't use the value with A label more than 2 times.

"""

import heapq


# O(NlogK)
def k_largerst(values, labels, k, m):
    entity = {}

    for value, label in zip(values, labels):
        pq = entity.get(label, [])
        heapq.heappush(pq, -value)

        if len(pq) > m:
            pq.pop()

        entity[label] = pq

    result = []
    for pq in entity.values():
        for val in pq:
            result.append(-val)
            if len(result) > k:
                result.pop()

    return result


def test1():
    values = [9, 8, 6, 8, 7]
    labels = ['A', 'A', 'B', 'A', 'B']
    k = 3
    m = 2
    expected = [9, 8, 7]
    actual = k_largerst(values, labels, k, m)
    assert actual == expected, 'Incorrect answer'
    print('Correct answer')


def test2():
    values = [9, 8, 6, 8, 7]
    labels = ['A', 'A', 'B', 'A', 'C']
    k = 3
    m = 1
    expected = [9, 6, 7]
    actual = k_largerst(values, labels, k, m)
    assert actual == expected, 'Incorrect answer'
    print('Correct answer')


test1()
test2()
