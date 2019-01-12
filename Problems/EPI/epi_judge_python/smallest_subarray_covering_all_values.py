import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph, keywords):
    result = Subarray(-1, -1)
    data_keywords = {s: i for i, s in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    shortest_subarray_length = [float('inf')] * len(keywords)
    shortest_distance = float('inf')

    for i, p in enumerate(paragraph):
        if p in data_keywords:
            keyword_idx = data_keywords[p]
            if keyword_idx == 0:
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
                distance_to_prev_keyword = (i - latest_occurrence[keyword_idx - 1])
                shortest_subarray_length[keyword_idx] = distance_to_prev_keyword + \
                                                        shortest_subarray_length[keyword_idx - 1]
            latest_occurrence[keyword_idx] = i

            if keyword_idx == len(keywords) - 1 and shortest_subarray_length[-1] < shortest_distance:
                shortest_distance = shortest_subarray_length[-1]
                result = Subarray(i - shortest_distance + 1, i)

    return result


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
