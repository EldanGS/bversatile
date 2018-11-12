import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    s.reverse()
    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

    start = 0
    n = len(s)
    while True:
        end = s.find(b' ', start)
        if end == -1:
            break

        reverse_range(s, start, end - 1)
        print(start, end, s[start:end])
        start = end + 1

    reverse_range(s, start, n - 1)
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("6-06-reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
