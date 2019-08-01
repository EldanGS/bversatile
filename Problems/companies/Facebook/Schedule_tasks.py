# https://leetcode.com/discuss/interview-question/338948/Facebook-or-Onsite-or-Schedule-of-Tasks

"""
You are given a schedule of tasks to work on. Each tasks has a start and an end time [start, end] where end > start. Find out for the given schedule:

in what intervals you are working (at least 1 task ongoing)
in what intervals you are multitasking (at least 2 tasks ongoing)
In other words, find union and intersection of a list of intervals. The input is sorted by start time.

Example:
Input: [[1, 10], [2, 6], [9, 12], [14, 16], [16, 17]]

Output union: [[1, 12], [14, 17]]
Explanation: We just need to merge overlapping intervals https://leetcode.com/problems/merge-intervals

Output intersection: [[2, 6], [9, 10]]

"""


def interval_intersections(intervals) -> list:
    if not intervals:
        return []

    intervals.sort()
    intersections = []
    start, end = intervals[0][0], intervals[0][1]

    for cur_start, cur_end in intervals[1:]:
        if end > cur_start:
            intersections.append([max(start, cur_start), min(end, cur_end)])
            end = max(end, cur_end)
        else:
            start, end = cur_start, cur_end

    return intersections


def __test(intervals, expected):
    actual = interval_intersections(intervals)

    assert actual == expected, 'Wrong answer'
    print('Accepted')


if __name__ == '__main__':
    intervals = [[1, 10], [2, 6], [9, 12], [14, 16], [16, 17]]
    __test(intervals, [[2, 6], [9, 10]])

    intervals = [[1, 10], [2, 6], [9, 12], [11, 16], [16, 17]]
    __test(intervals, [[2, 6], [9, 10], [11, 12]])

    intervals = [[1, 10], [2, 6], [9, 12], [14, 16], [15, 17]]
    __test(intervals, [[2, 6], [9, 10], [15, 16]])

