import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    count_a, idx = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[idx] = s[i]
            idx += 1
        if s[i] == 'a':
            count_a += 1

    cur_idx = idx - 1
    idx += count_a - 1
    final_size = idx + 1

    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[idx - 1:idx + 1] = 'dd'
            idx -= 2
        else:
            s[idx] = s[cur_idx]
            idx -= 1
        cur_idx -= 1

    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("6-04-replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
