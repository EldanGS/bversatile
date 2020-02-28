"""
https://leetcode.com/discuss/interview-question/519744/Microsoft-Telephonic-round
Had my Microsoft telephonic round.

You are given a array of strings, to have to group them based on similar anagrams,
with duplicates removed, with additional constraints: Characters can be capital and small.

Example:
{'Good', "pan", "nap", "dog", "god"}

Output
[['Good', 'dog', 'god'],
['nap', 'pan']]
"""
from collections import defaultdict


def normalize(word):
    return tuple(set(word.lower()))


def group_words(words):
    groups = defaultdict(list)
    for word in words:
        normalized_word = normalize(word)
        groups[normalized_word].append(word)

    return list(groups.values())


def _test_group_words(words, expected):
    actual = group_words(words)
    assert actual.sort() == expected.sort(), f'Wrong answer, {actual}'
    print('Passed', actual, expected)


if __name__ == '__main__':
    words = {'Good', "pan", "nap", "dog", "god"}
    expected = [['Good', 'dog', 'god'], ['nap', 'pan']]
    _test_group_words(words, expected)
