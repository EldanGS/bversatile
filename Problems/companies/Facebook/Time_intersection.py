"""
Time Intersection
Description

Give two users' ordered online time series, and each section records the user's login time point x and offline time point y.
Find out the time periods when both users are online at the same time, and output in ascending order.
You need return a list of intervals.

We guarantee that the length of online time series meet 1 <= len <= 1e6.
For a user's online time series, any two of its sections do not intersect.
Example

Example 1:

Input: seqA = [(1,2),(5,100)], seqB = [(1,6)]
Output: [(1,2),(5,6)]
Explanation: In these two time periods (1,2), (5,6), both users are online at the same time.
Example 2:

Input: seqA = [(1,2),(10,15)], seqB = [(3,5),(7,9)]
Output: []
Explanation: There is no time period, both users are online at the same time.

"""


def time_intersection(A, B):
    if not A or not B:
        return A or B

    timelines = []
    for start, end in A:
        timelines.append((start, 0))
        timelines.append((end, 1))

    for start, end in B:
        timelines.append((start, 0))
        timelines.append((end, 1))

    timelines.sort()

    result, count = [], 0

    for i, (time, delta) in enumerate(timelines):
        if delta == 0:
            count += 1
        else:
            count -= 1

        if count == 2:
            result.append((time, timelines[i + 1][0]))

    return result


if __name__ == '__main__':
    A = [(1, 2), (5, 100)]
    B = [(1, 6)]
    print(time_intersection(A, B))

    A = [(1, 2), (10, 15)]
    B = [(3, 5), (7, 9)]
    print(time_intersection(A, B))
