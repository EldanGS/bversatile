# https://leetcode.com/problems/unique-morse-code-words/description/

# hard code <3 ;D not elegant
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        data = dict()
        for index, c in enumerate(ascii_lowercase):
            data[c] = morse[index]
        
        unique_morse = list()
        for word in words:
            text = ''
            for c in word:
                text += data[c]
            unique_morse.append(text)
        
        return len(set(unique_morse))

# python elegant style
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
        "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        return len({''.join(morse[ord(c) - ord('a')] for c in word) for word in words})