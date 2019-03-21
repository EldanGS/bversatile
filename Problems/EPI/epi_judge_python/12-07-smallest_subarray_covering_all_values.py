import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))
INFINITY = float('inf')


def find_smallest_sequentially_covering_subset(paragraph, keywords):
    keyword_to_index = {word: index for index, word in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    shortest_subarray_distance = [INFINITY] * len(keywords)
    shortest_distance = INFINITY
    result = Subarray(-1, -1)

    for i, p in enumerate(paragraph):
        if p in keyword_to_index:
            keyword_index = keyword_to_index[p]
            if keyword_index == 0:
                shortest_subarray_distance[keyword_index] = 1
            elif shortest_subarray_distance[keyword_index - 1] != INFINITY:
                distance_to_prev_keyword = (i - latest_occurrence[keyword_index - 1])
                shortest_subarray_distance[keyword_index] = (distance_to_prev_keyword +
                                                             shortest_subarray_distance[keyword_index - 1])

            latest_occurrence[keyword_index] = i

            if keyword_index == len(keywords) - 1 and shortest_subarray_distance[-1] < shortest_distance:
                shortest_distance = shortest_subarray_distance[-1]
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
            "12-07-smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
