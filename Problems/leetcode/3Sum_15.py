# https://leetcode.com/problems/3sum/


# O(N^2) time, O(1) space
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n, triplet = len(nums), []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            target = 0 - nums[i]
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    temp = [nums[i], nums[left], nums[right]]
                    triplet.append(temp)

                    while left < right and nums[left] == temp[1]:
                        left += 1
                    while left < right and nums[right] == temp[2]:
                        right -= 1

                elif current_sum > target:
                    right -= 1
                else:
                    left += 1

        return triplet
