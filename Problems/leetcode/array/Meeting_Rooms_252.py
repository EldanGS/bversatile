# https://www.leetfree.com/problems/meeting-rooms.html#

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def meeting(self, intervals):
    	if not intervals:
    		return False

    	n = len(intervals)
    	intervals.sort(key = lambda x: x.start)
    	start = intervals[0].start
    	end = intervals[0].end

    	for i in range(1, n):
    		if end >= intervals[i].start:
    			return False
    		start = intervals[i].start
    		end = intervals[i].end

    	return True
 
