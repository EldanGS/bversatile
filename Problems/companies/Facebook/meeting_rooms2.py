"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""
import heapq


def meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals.sort()
    free_rooms = []
    heapq.heappush(free_rooms, intervals[0][1])

    for start, end in intervals[1:]:
        if start >= free_rooms[0]:
            heapq.heappop(free_rooms)

        heapq.heappush(free_rooms, end)

    return len(free_rooms)


def __test(intervals, expected):
    actual = meeting_rooms(intervals)

    assert actual == expected, 'Wrong answer'
    print('Accepted')


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    __test(intervals, 2)

    intervals = [[0, 30]]
    __test(intervals, 1)

    intervals = [[0, 10], [10, 20], [20, 30]]
    __test(intervals, 1)

    intervals = [[0, 10], [9, 20], [15, 30]]
    __test(intervals, 2)