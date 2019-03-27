from test_framework import generic_test


def buy_and_sell_stock_k_times(prices, k):
    if not k:
        return 0.0
    elif 2 * k >= len(prices):
        max_profit = 0.0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit

    min_prices, max_profits = [float('inf')] * k, [0] * k
    for price in prices:
        for i in reversed(list(range(k))):
            max_profits[i] = max(max_profits[i], price - min_prices[i])
            min_prices[i] = min(min_prices[i], price - (0 if i == 0 else max_profits[i - 1]))

    return max_profits[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("24-03-buy_and_sell_stock_k_times.py",
                                       'buy_and_sell_stock_k_times.tsv',
                                       buy_and_sell_stock_k_times))
