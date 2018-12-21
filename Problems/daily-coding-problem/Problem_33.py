"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers,
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""
from heapq import *


class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def add_num(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def find_median(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2


if __name__ == '__main__':
    A = [2, 1, 5, 7, 2, 0, 5]
    median = MedianFinder()
    for a in A:
        median.add_num(a)
        print(median.find_median())
