import functools
from collections import deque

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class QueueWithMax:
    def __init__(self):
        self._entries = deque()
        self._candidates_for_max = deque()

    def enqueue(self, x):
        self._entries.append(x)
        while self._candidates_for_max and self._candidates_for_max[-1] < x:
            self._candidates_for_max.pop()
        self._candidates_for_max.append(x)

    def dequeue(self):
        if self._entries:
            result = self._entries.popleft()
            if result == self._candidates_for_max[0]:
                self._candidates_for_max.popleft()
            return result

        raise IndexError('Empty queue')

    def max(self):
        if self._candidates_for_max:
            return self._candidates_for_max[0]


class TrafficElement:
    def __init__(self, time, volume):
        self.time = time
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume

    def __eq__(self, other):
        return self.time == other.time and self.volume == other.volume


def calculate_traffic_volumes(A, w):
    sliding_window = QueueWithMax()
    maximum_volumes = []
    for traffic_info in A:
        sliding_window.enqueue(traffic_info)
        while traffic_info.time - sliding_window.max().time > w:
            sliding_window.dequeue()

        maximum_volumes.append(TrafficElement(traffic_info.time, sliding_window.max().volume))

    return maximum_volumes


@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

    return [(x.time, x.volume) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("24-12-max_of_sliding_window.py",
                                       'max_of_sliding_window.tsv',
                                       calculate_traffic_volumes_wrapper))
