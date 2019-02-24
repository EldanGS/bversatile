# https://leetcode.com/problems/continuous-subarray-sum/


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        run_sum = 0
        seen = {0: -1}
        for i, num in enumerate(nums):
            run_sum = (run_sum + num) % k if k else run_sum + num

            if run_sum not in seen:
                seen[run_sum] = i

            if i - seen[run_sum] > 1:
                return True

        return False
