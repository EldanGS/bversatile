# https://leetcode.com/problems/majority-element/description/

"""
1st solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - always
"""
class Solution:
    def majorityElement(self, nums):
	    n = len(nums)
        count = n // 2
        data = dict()
        
        for num in nums:
            if not data.get(num):
                data[num] = 1
            else:
                data[num] += 1
        
        result = None
        for val, freq in data.items():
            if freq > count:
                result = val
        
        return result


"""
2nd solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - always
"""
class Solution:
    def majorityElement(self, nums):
        count = len(nums) // 2
        data = dict()
        result = None
        
        for num in nums:
            if not data.get(num):
                data[num] = 1
            else:
                data[num] += 1
            if data[num] > count:
                result = num
        
        return result

"""
3th solution, optimal and concise
Complexity analysis:
Time: O(N) - always
Memory: O(1) - always
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        selected_num = nums[0]
        freq = len(nums) // 2
        count = 0
        
        for num in nums:
            if count > freq:
                return selected_num
                
            if num == selected_num:
                count += 1
            elif count == 1:
                selected_num = num
            else:
                count -= 1
            
        return selected_num