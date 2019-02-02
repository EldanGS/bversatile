from test_framework import generic_test


# O(N) time, O(1) space
def buy_and_sell_stock_once(prices):
    if not prices:
        raise ValueError('Stock prices does not exists')

    min_daily_price, max_profit = prices[0], 0
    for price in prices[1:]:
        min_daily_price = min(min_daily_price, price)
        max_profit = max(max_profit, price - min_daily_price)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("05-06-buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
