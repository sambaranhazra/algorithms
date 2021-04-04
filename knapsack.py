#!/usr/bin/env python3
def profit(weights: int, prices: int, size: int, n: int, cache: list):
    if size == 0 or n == 0:
        return 0
    if cache[size][n] != 0:
        return cache[n][size]
    if size >= weights[n - 1]:
        cache[size][n] = max(
            profit(weights, prices, size, n - 1, cache),
            prices[n - 1]
            + profit(weights, prices, size - weights[n - 1], n - 1, cache),
        )
    else:
        cache[size][n] = profit(weights, prices, size, n - 1, cache)
    return cache[size][n]


def main():
    weights = [4, 5, 1, 4]
    prices = [1, 2, 3, 2]
    size = 6
    cache = [[0 for _ in range(len(weights) + 1)] for _ in range(size + 1)]
    print("The max profit is", profit(weights, prices, size, len(weights), cache))


if __name__ == "__main__":
    main()
