# https://leetcode.com/problems/moving-average-from-data-stream/description/

"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.


Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

"""

class MovingAverage:

    def __init__(self, size: 'int'):
        """
        Initialize your data structure here.
        """
        self.entity = [0] * size
        self.size = size
        self.sum, self.index = 0, 0

    def next(self, val: 'int') -> 'float':
        self.index += 1
        self.sum -= self.entity[self.index % self.size]
        self.entity[self.index % self.size] = val

        self.sum += val

        return self.sum / min(self.index, self.size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)