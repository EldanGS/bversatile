# https://leetcode.com/problems/detect-capital/description/

# Quick solve, not optimal, O(3N) ~ O(N) by time, O(1) by space
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():
            return True
        
        first_up = word[0].isupper()
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
        
        return first_up


# Little bit optimal, O(N) by time, O(1) by space
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0
        for c in word:
            if c.isupper():
                count += 1
        
        return (count == 0 or count == len(word)) or (count == 1 and word[0].isupper())
 

# Elegant solution with Python methods, but slow O(3N) ~ O(N)
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return (word.isupper() or word.islower() or word.istitle())

