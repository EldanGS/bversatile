# https://leetcode.com/discuss/interview-question/124849/Facebook%3A-getNextMinimum-every-single-call

"""
You have three unsorted list of numbers.
list1 = {5,1,2,4}
list2 = {4,6,3}
list3 = {9,0,7}
Design/Write function that will return next minimum element out of these lists (remove that element from list)
Our function should return: 0,1,2,3,4,4,5,6,7,9 on repetitive calls

Don't even think about brute force solution.

"""

import heapq
import collections


ValueAndIndex = collections.namedtuple('ValueAndIndex', ('value', 'index', 'list_num'))


class GetNextMin:

    def __init__(self, l1, l2, l3):
        self.min_heap = []

        if l1:
            self.l1 = sorted(l1)
            heapq.heappush(self.min_heap, ValueAndIndex(value=self.l1[0], index=1, list_num=1))

        if l2:
            self.l2 = sorted(l2)
            heapq.heappush(self.min_heap, ValueAndIndex(value=self.l2[0], index=1, list_num=2))

        if l3:
            self.l3 = sorted(l3)
            heapq.heappush(self.min_heap, ValueAndIndex(value=self.l3[0], index=1, list_num=3))

    def has_next(self):
        return self.min_heap

    def next(self):
        if not self.has_next():
            raise IndexError

        value, index, list_num = heapq.heappop(self.min_heap)

        if list_num == 1:
            if index < len(self.l1):
                heapq.heappush(self.min_heap, (self.l1[index], index + 1, list_num))
        elif list_num == 2:
            if index < len(self.l2):
                heapq.heappush(self.min_heap, (self.l2[index], index + 1, list_num))
        else:
            if index < len(self.l3):
                heapq.heappush(self.min_heap, (self.l3[index], index + 1, list_num))

        return value


if __name__ == '__main__':
    l1, l2, l3 = [5,1,2,4], [4,6,3], [9,0,7]
    solution = GetNextMin(l1, l2, l3)

    for _ in range(10):
        print('current min:', solution.next())
