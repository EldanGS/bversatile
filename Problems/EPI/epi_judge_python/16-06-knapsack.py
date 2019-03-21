import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    n, capacity = len(items) + 1, capacity + 1
    dp = [[0] * capacity for _ in range(n)]
    for i in range(1, n):
        for weight in range(1, capacity):
            if items[i - 1].weight <= weight:
                dp[i][weight] = max(dp[i - 1][weight],
                                    dp[i - 1][weight - items[i - 1].weight] + items[i - 1].value)
            else:
                dp[i][weight] = dp[i - 1][weight]

    return dp[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-06-knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
