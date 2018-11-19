from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    min_price, max_profit = prices[0], 0.0
    for price in prices[1:]:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("5-06-buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
