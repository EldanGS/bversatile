# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

"""
1st solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - worst case
"""
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = []
        data = dict()
        for i, num in enumerate(numbers):
            aim = target - num
            if data.get(aim):
                pos.append(data[aim])
                pos.append(i + 1)
                break
                
            data[num] = i + 1
        
        return pos


"""
2nd solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = []
        left, right = 0, len(numbers) - 1
        
        while left < right:
            temp = target - (numbers[left] + numbers[right])
            if temp < 0:
                right -= 1
            elif temp > 0:
                left += 1
            else:
                pos.append(left + 1)
                pos.append(right + 1)
                break
        
        return pos
