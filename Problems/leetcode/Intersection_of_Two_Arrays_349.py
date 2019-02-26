# https://leetcode.com/problems/intersection-of-two-arrays/


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        s = set(nums1)
        return list({x for x in nums2 if x in s})