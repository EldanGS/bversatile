// https://leetcode.com/problems/self-dividing-numbers/description/

"""
Solution.
Complexity analysis:
Time: O(NlogN) - always
Memory: O(N) - in worst case
"""

class Solution {
public:
    bool check(int value) {
        if (value < 10) {
            return true;
        }
        
        for (int num = value; num > 10; num /= 10) {
            if (!(num % 10) or value % (num % 10)) {
                return false;
            }
        }
        
        return true;
    }
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> result;
        for (int i = left; i <= right; i++) {
            if (check(i)) {
                result.push_back(i);
            }
        }
        
        return result;
    }
};