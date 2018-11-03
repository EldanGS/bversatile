from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    max_total_profit, min_price = 0, float('inf')
    n = len(prices)
    first_buy = [0] * n
    for i, price in enumerate(prices):
        min_price = min(min_price, price)
        max_total_profit = max(max_total_profit, price - min_price)
        first_buy[i] = max_total_profit

    max_price = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price = max(max_price, price)
        max_total_profit = max(max_total_profit, max_price - price + first_buy[i - 1])

    return max_total_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("5-07-buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
