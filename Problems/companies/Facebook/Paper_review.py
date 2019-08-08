# https://www.leetfree.com/problems/sentence-similarity-ii.html

"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar,
if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:
The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].

"""
from collections import defaultdict


# O(N * M) time, where N is length of words, M is length of pairs
# O(M) space, where M is length of pairs
def are_sentences_similar_two(words1: list, words2: list, pairs):
    if len(words1) != len(words2):
        return False

    graph = defaultdict(set)
    for u, v in pairs:
        graph[u].add(v)
        graph[v].add(u)

    for w1, w2 in zip(words1, words2):
        stack, visited = [w1], {w1}

        while stack:
            cur_word = stack.pop()

            if cur_word == w2:
                break

            for neighbor in graph[cur_word]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        else:
            return False

    return True


def _test(words1, words2, pairs, expected):
    actual = are_sentences_similar_two(words1, words2, pairs)

    assert actual == expected, 'Wrong answer'
    print('Accepted')


if __name__ == '__main__':
    words1 = ["great", "acting", "skills"]
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]]

    _test(words1, words2, pairs, True)

    words1 = ["great", "acting", "skills"]
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "tal"]]

    _test(words1, words2, pairs, False)
