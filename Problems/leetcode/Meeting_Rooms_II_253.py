# https://www.leetfree.com/problems/meeting-rooms-ii.html#
import heapq


class Interval:
    def __init__(self, start, end):
        self.start, self.end = start, end


def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda interval: interval.start)

    min_heap = [intervals[0].end]
    for interval in intervals[1:]:
        if interval.start >= min_heap[0]:
            heapq.heappushpop(min_heap, interval.end)
        else:
            heapq.heappush(min_heap, interval.end)

    return len(min_heap)


if __name__ == '__main__':
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20), Interval(20, 30)]
    print(min_meeting_rooms(intervals))
