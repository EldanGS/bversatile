from test_framework import generic_test


def maximum_revenue(coins):
    n = len(coins)
    maximum_revenue_for_range = [[0] * n for _ in coins]
    for gap in range(n):
        i, j = 0, gap
        while j < n:
            x = maximum_revenue_for_range[i + 2][j] if i + 2 <= j else 0
            y = maximum_revenue_for_range[i + 1][j - 1] if i + 1 <= j - 1 else 0
            z = maximum_revenue_for_range[i][j - 2] if i <= j - 2 else 0
            maximum_revenue_for_range[i][j] = max(coins[i] + min(x, y), coins[j] + min(y, z))

            i, j = i + 1, j + 1

    return maximum_revenue_for_range[0][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "16---picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
