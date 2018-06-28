"""
Note:
	You must not modify the array (assume the array is read only).
	You must use only constant, O(1) extra space.
	Your runtime complexity should be less than O(n^2).
	There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        slow = n
        fast = n
        while True:
            slow = nums[slow - 1]
            fast = nums[nums[fast - 1] - 1]
            
            if slow == fast:
                break
        
        slow = n
        while slow != fast:
            slow = nums[slow - 1]
            fast = nums[fast - 1]
        
        return slow
        
# Emulate do-while loop in Python: https://coderwall.com/p/q_rd1q/emulate-do-while-loop-in-python