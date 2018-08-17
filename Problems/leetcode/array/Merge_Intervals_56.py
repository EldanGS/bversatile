# https://leetcode.com/problems/merge-intervals/description/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


"""
Solution.
Complexity analysis:
Time: O(NlogN) - in worst case
Memory: O(N) - always
"""
class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        intervals.sort(key = lambda x: x.start)
        result = []
        n = len(intervals)
        start = intervals[0].start
        end = intervals[0].end
        
        for i in range(n):
            if end >= intervals[i].start:
                end = max(end, intervals[i].end)
            else:
                result.append(Interval(start, end))
                start = intervals[i].start
                end = intervals[i].end
        
        result.append(Interval(start, end))
        
        return result

