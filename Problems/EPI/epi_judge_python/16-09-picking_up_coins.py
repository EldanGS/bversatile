from test_framework import generic_test


def maximum_revenue(coins: []) -> int:
    def compute_maximum_revenue_for_range(a, b):
        if a > b:
            return 0

        if dp[a][b] == 0:
            max_revenue_a = coins[a] + min(compute_maximum_revenue_for_range(a + 2, b),
                                           compute_maximum_revenue_for_range(a + 1, b - 1))
            max_revenue_b = coins[b] + min(compute_maximum_revenue_for_range(a + 1, b - 1),
                                           compute_maximum_revenue_for_range(a, b - 2))

            dp[a][b] = max(max_revenue_a, max_revenue_b)
        return dp[a][b]

    dp = [[0] * len(coins) for _ in coins]
    return compute_maximum_revenue_for_range(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "16-09-picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
