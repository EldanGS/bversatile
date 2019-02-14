# https://leetcode.com/problems/merge-intervals/
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval.start)

        current_start, current_end = intervals[0].start, intervals[0].end
        merged_intervals = []

        for interval in intervals[1:]:
            if current_end >= interval.start:
                current_end = max(current_end, interval.end)
            else:
                merged_intervals.append(Interval(current_start, current_end))
                current_start, current_end = interval.start, interval.end

        merged_intervals.append(Interval(current_start, current_end))
        return merged_intervals
