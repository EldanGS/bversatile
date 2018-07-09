# https://leetcode.com/problems/judge-route-circle/description/

# O(N) by time, O(1) by space
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_UW = 0
        move_LR = 0
        for c in moves:
            if c == 'U':
                move_UW += 1
            elif c == 'D':
                move_UW -= 1
            elif c == 'L':
                move_LR += 1
            elif c == 'R':
                move_LR -= 1
        
        return (move_UW == 0 and move_LR == 0)

