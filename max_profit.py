#!/usr/bin/env python3
def max_profit(prices, k, n):
    if n == 0 or k == 0:
        return 0
    profit = 0
    price = prices[n - 1]
    for i in range(n - 1):
        profit = max(profit, price - prices[i] + max_profit(prices, k - 1, i))
    return profit


def max_profit_with_k_transactions(prices, k):
    return max_profit(prices, k, len(prices))
