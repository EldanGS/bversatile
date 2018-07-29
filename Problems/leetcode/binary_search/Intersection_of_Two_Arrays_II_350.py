# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

"""
1st solution.
Complexity analysis:
Time: O(N + M) - always
Memory: O(N + M) - in worst case
"""

class Solution:
    def intersect(self, nums1, nums2):
        data = dict()
        for num in nums1:
            if not data.get(num):
                data[num] = 1
            else:
                data[num] += 1
        
        inter = []
        for num in nums2:
            if data.get(num):
                data[num] -= 1
                inter.append(num)
        
        return inter

"""
2nd solution.
Complexity analysis:
Time: O(max(N, M) * log(max(N, M))) - in worst case
Memory: O(N + M) - in worst case
"""

class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        n1, n2 = len(nums1), len(nums2)
        i1, i2 = 0, 0
        inter = []
        
        while i1 < n1 and i2 < n2:
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                inter.append(nums1[i1])
                i1 += 1
                i2 += 1
                
        return inter