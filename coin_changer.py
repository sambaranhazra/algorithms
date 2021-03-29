#!/usr/bin/env python3

def ways(coins, total, n, cache):
    if total == 0:
        return 1
    if n == 0:
        return 0
    if cache[total][n] != 0:
        return cache[total][n]

    if total < coins[n - 1]:
        cache[total][n] = ways(coins, total, n - 1, cache)
    else:
        cache[total][n] = ways(coins, total - coins[n - 1], n, cache) + ways(coins, total, n - 1, cache)
    return cache[total][n]


def main():
    coins = [1, 2, 3, 5, 10, 20]
    total = 4000
    cache = [[0 for _ in range(len(coins) + 1)] for _ in range(total + 1)]
    print(ways(coins, total, len(coins), cache))


if __name__ == '__main__':
    main()
