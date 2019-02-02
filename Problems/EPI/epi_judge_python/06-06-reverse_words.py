import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    s.reverse()

    def reverse_part(s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    left = 0
    while True:
        right = s.find(b' ', left)
        if right < 0:
            break
        reverse_part(s, left, right - 1)
        left = right + 1

    reverse_part(s, left, len(s) - 1)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("06-06-reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
