"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""


# O(NlogN)
def minimum_rooms(A):
    if not A:
        return 0

    intervals = {}
    for (start, end) in A:
        intervals[start] = intervals.get(start, 0) + 1
        intervals[end] = intervals.get(end, 0) - 1

    sorted_intervals = sorted(intervals.items())
    max_rooms, rooms = 0, 0
    for key, value in sorted_intervals:
        rooms += value
        max_rooms = max(max_rooms, rooms)

    return max_rooms


if __name__ == '__main__':
    A = [(30, 75), (0, 50), (60, 150)]
    A = [(0, 30), (5, 10), (15, 20)]
    print(minimum_rooms(A))
