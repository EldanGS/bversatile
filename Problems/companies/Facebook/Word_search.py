# https://leetcode.com/problems/add-and-search-word-data-structure-design/

"""
Given an array of words define a function that takes in a string and returns a boolean on whether or not that string is in the array. The function also must support search terms that contain “wild cards”. These are placeholders for any character and will be represented by the “.” symbol. The function must return true if the array contains the string passed into the function. If the string passed in contains a wildcard, every character to the left and right of the wild card must match up with the characters in one of the strings in the array. For example:

[“cat”, “dog”, “fish”, … ]

// Given the list above, we should get the following outputs
“cat” -> true
“cot” -> false
“c.t” -> true
“.og” -> true
“.do” -> false
“fis.” -> true
“fishy” -> false

"""
import string


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()

            node = node.child[c]

        node.is_word = True

    def search(self, word):
        stack = [(self.root, word)]

        while stack:
            node, w = stack.pop()

            if not w:
                if node.is_word:
                    return True
            elif w[0] == '.':
                for n in node.child.values():
                    stack.append((n, w[1:]))
            else:
                if w[0] in node.child:
                    n = node.child[w[0]]
                    stack.append((n, w[1:]))

        return False


def word_search(words, query):
    trie = Trie()

    for word in words:
        trie.insert(word)

    result = []
    for word in query:
        if trie.search(word):
            result.append(True)
        else:
            result.append(False)

    return result


def _test(words, query, expected):
    actual = word_search(words, query)

    assert actual == expected, 'Wrong Answer: {}'.format(actual)
    print('Accept')


if __name__ == '__main__':
    words = ["cat", "dog", "fish", "dat"]
    query = ["cat", "c.t", ".og", "fis.", "cot", "dot", "fish."]

    expected = [True, True, True, True, False, False, False]

    _test(words, query, expected)
