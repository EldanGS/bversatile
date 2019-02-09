import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    if not domain:
        return []

    n = len(domain)
    last_length = [-1] * n
    for i in range(n):
        if domain[:i + 1] in dictionary:
            last_length[i] = i + 1

        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and domain[j + 1:i + 1] in dictionary:
                    last_length[i] = i - j
                    break
    decomposition = []
    if last_length[-1] != -1:
        idx = len(domain) - 1
        while idx >= 0:
            decomposition.append(domain[idx + 1 - last_length[idx]: idx + 1])
            idx -= last_length[idx]
        decomposition = decomposition[::-1]

    return decomposition


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "16-07-is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
