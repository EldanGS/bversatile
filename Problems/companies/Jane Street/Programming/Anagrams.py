"""
Solution, more effective
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
"""

class Solution:
    def convert(self, word):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, \
                  41, 43, 47, 53, 59, 61, 67, 71, \
                  73, 79, 83, 89, 97, 101, 103 
                 ];
        value = 1
        for c in word:
            value *= primes[ord(c) - 97]
        
        return value
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        data = dict()
        result = list()
        
        for s in strs:
            temp = self.convert(s)
            if not data.get(temp):
                data[temp] = [s]
            else:
                data[temp].append(s)
        
        for key, value in data.items():
            result.append(value)
            
        return result