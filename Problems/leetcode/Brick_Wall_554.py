# https://leetcode.com/problems/brick-wall/description/

"""
Solution, more effective
Complexity analysis:
Time: O(NM) always
Memory: O(M) in worst case
"""
class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        data = collections.defaultdict(int)
        line = 0
        for bricks in wall:
            weight = 0
            for brick in bricks[:-1]:
                weight += brick
                data[weight] += 1
                line = max(line, data[weight])
        
        return len(wall) - line
