# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

"""
Solution.
Complexity analysis:
Time: O(logN) - always
Memory: O(1) - always
"""

class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        answer = []
        
        while left < right:
            current = target - numbers[left] - numbers[right]
            if current > 0:
                left += 1
            elif current < 0:
                right -= 1
            else:
                answer.append(left + 1)
                answer.append(right + 1)
                break
        
        return answer
