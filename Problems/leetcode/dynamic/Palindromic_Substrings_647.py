# https://leetcode.com/problems/palindromic-substrings/description/

"""
1st solution.
Complexity analysis:
Time: O(N^2) - in worst case
Memory: O(1) - always
"""

class Solution:
    def countSubstrings(self, s):
        n = len(s)
        count = 0
        
        for mid in range(n * 2 - 1):
            left = mid // 2
            right = left + (mid & 1)
            
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count

"""
2nd solution, Manacher algorithm. (https://cp-algorithms.com/string/manacher.html)
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - always
"""

class Solution:
    def countSubstrings(self, s):
        s = '@#' + '#'.join(s) + '#$' # @ - left bound, $ - right bound
        n = len(s)
        ro = [0] * n
        left, right = 0, 0
        
        for i in range(1, n - 1):
            if i < right:
                ro[i] = min(right - i, ro[left * 2 - i])
            
            while s[i - ro[i] - 1] == s[i + ro[i] + 1]:
                ro[i] += 1
            
            if i + ro[i] > right:
                left, right = i, i + ro[i]
        
        return sum((val + 1) // 2 for val in ro)
