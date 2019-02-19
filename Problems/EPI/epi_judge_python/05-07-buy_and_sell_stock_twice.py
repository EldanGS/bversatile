from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    if not prices:
        return 0

    n = len(prices)
    min_price_so_far, max_price_so_far = float('inf'), 0
    forward_trade = [0] * n
    for i in range(n):
        min_price_so_far = min(min_price_so_far, prices[i])
        max_price_so_far = max(max_price_so_far, prices[i] - min_price_so_far)
        forward_trade[i] = max_price_so_far

    max_total_profit, max_price_so_far = 0.0, float('-inf')
    for i, price in reversed(list(enumerate(prices, 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit,
                               max_price_so_far - price + forward_trade[i - 1])

    return max_total_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("05-07-buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
