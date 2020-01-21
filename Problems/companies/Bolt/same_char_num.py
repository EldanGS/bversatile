"""
Check if string contains the exact same number of repetitions of every character.
I.e. "aabb" - true, "aabbc" - false.

Then check if removing a single character from the string can make it valid,
i.e. "aabbc" - true, "aaabbbcc" - false
"""

from collections import Counter


def same_char_frequency(word: str) -> bool:
    counter = Counter(word)
    current_count = -1
    for count in counter.values():
        if current_count == -1:
            current_count = count
        elif current_count != count:
            return False
    return True


def _test_same_char_frequency(word, expected):
    actual = same_char_frequency(word)
    assert actual == expected, 'Wrong answer, {} != {}'.format(expected, actual)
    print('accepted')


def _test_same_char_frequency_after_removing_one_char(word, expected):
    actual = remove_one_char_to_make_word_frequency_same(word)
    assert actual == expected, 'Wrong answer, {} != {}'.format(expected, actual)
    print('accepted')


def get_word_removed_one_char(word: str, counter: dict, remain: int) -> str:
    for i, c in enumerate(word):
        if counter[c] % 2 == remain:
            return "".join(word[:i] + word[i + 1:])
    return word


def remove_one_char_to_make_word_frequency_same(word: str) -> bool:
    counter = Counter(word)
    even, odd = 0, 0
    for count in counter.values():
        if count % 2 == 0:
            even += 1
        else:
            odd += 1

    if even > odd:
        word = get_word_removed_one_char(word, counter, 1)
    elif even < odd:
        word = get_word_removed_one_char(word, counter, 0)

    return same_char_frequency(word)


if __name__ == '__main__':
    print('Test same word frequency')
    word = "aabb"
    _test_same_char_frequency(word, True)
    word = "aabbc"
    _test_same_char_frequency(word, False)
    word = "aabbcc"
    _test_same_char_frequency(word, True)
    word = ""
    _test_same_char_frequency(word, True)
    word = "aabbbccc"
    _test_same_char_frequency(word, False)

    print('Test same word frequency after removing one char')
    word = "aabb"
    _test_same_char_frequency_after_removing_one_char(word, True)
    word = "aabbc"
    _test_same_char_frequency_after_removing_one_char(word, True)
    word = "aabbcc"
    _test_same_char_frequency_after_removing_one_char(word, True)
    word = ""
    _test_same_char_frequency_after_removing_one_char(word, True)
    word = "aabbbccc"
    _test_same_char_frequency_after_removing_one_char(word, False)
