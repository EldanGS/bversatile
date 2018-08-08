# https://leetcode.com/problems/letter-case-permutation/description/

"""
1st solution. Python3
Complexity analysis:
Time: O(N^2) - always
Memory: O(N) - always
"""

class Solution:
    def backtrack(self, s, result, index):  
        if index >= len(s):
            return
        
        result.append(''.join(s))
        for i in range(index, len(s)):
            if s[i].isalpha():
                s[i] = s[i].upper()
                self.backtrack(s, result, i + 1)
                s[i] = s[i].lower()
        
    def letterCasePermutation(self, S):
        result = []
        self.backtrack(list(S), result, 0)
        return result


"""
2nd solution. Cpp17
Complexity analysis:
Time: O(N^2) - always
Memory: O(N) - always
"""

class Solution {
public:
    void backtrack(string s, vector<string>& result, int index) {
        result.push_back(s);
        if (index >= s.size()) {
            return;
        }
        
        for (int i = index; i < (int)s.size(); i++) {
            if (isalpha(s[i])) {
                s[i] ^= 32; # to upper
                backtrack(s, result, i + 1);
                s[i] ^= 32; # to lower
            }
        }
    }
    vector<string> letterCasePermutation(string S) {
        vector<string> result;
        backtrack(S, result, 0);
        return result;
    }
};
