import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


# My solution
def optimum_subject_to_capacity1(items, capacity):
    dp = [[0] * (capacity + 1) for _ in range(len(items) + 1)]
    for i in range(len(items) + 1):
        for weight in range(capacity + 1):
            if i == 0 or weight == 0:
                dp[i][weight] = 0
            elif items[i - 1].weight <= weight:
                dp[i][weight] = max(dp[i - 1][weight], dp[i - 1][weight - items[i - 1].weight] + items[i - 1].value)
            else:
                dp[i][weight] = dp[i - 1][weight]

    return dp[-1][-1]


# Author solution
def optimum_subject_to_capacity(items, capacity):
    def calculate_optimum_subject(k, available_capacity):
        if k < 0:
            # No items can be chosen.
            return 0
        if V[k][available_capacity] == -1:
            without_curr_utem = calculate_optimum_subject(k - 1, available_capacity)
            with_curr_item = (0 if available_capacity < items[k].weight
                              else (
                    items[k].value + calculate_optimum_subject(k - 1, available_capacity - items[k].weight)))
            V[k][available_capacity] = max(without_curr_utem, with_curr_item)
        return V[k][available_capacity]

    V = [[-1] * (capacity + 1) for _ in items]
    return calculate_optimum_subject(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-06-knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
