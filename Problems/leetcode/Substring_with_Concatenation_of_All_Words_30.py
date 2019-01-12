# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""
class Solution:
    def findSubstring(self, s, words):
        ans = []
        if (not s) or (not words):
            return ans
        
        data = dict()
        for word in words:
            if not data.get(word):
                data[word] = 1
            else:
                data[word] += 1
        
        n = len(s)
        num, wl = len(words), len(words[0])
        for i in range(0, n - num * wl + 1):
            seen = dict()
            j = 0
            while j < num:
                temp = s[i + j * wl: i + (j + 1) * wl]
                if not data.get(temp):
                    break
                else:
                    if not seen.get(temp):
                        seen[temp] = 1
                    else:
                        seen[temp] += 1
                    
                    if seen[temp] > data[temp]:
                        break
                j += 1
            if j == num:
                ans.append(i)
        
        return ans
                
