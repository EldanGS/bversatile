"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

"""


def meeting_rooms(intervals):
    if not intervals:
        return True

    intervals.sort()

    end = intervals[0][1]

    for cur_start, cur_end in intervals[1:]:
        if end > cur_start:
            return False

        end = cur_end

    return True


def __test(intervals, expected):
    actual = meeting_rooms(intervals)

    assert actual == expected, 'Wrong answer'
    print('Accepted')


if __name__ == '__main__':
    intervals = [[0, 30],[5, 10],[15, 20]]
    __test(intervals, False)

    intervals = [[0, 30]]
    __test(intervals, True)

    intervals = [[0, 10], [10, 20], [20, 30]]
    __test(intervals, True)

    intervals = [[0, 10], [9, 20], [15, 30]]
    __test(intervals, False)