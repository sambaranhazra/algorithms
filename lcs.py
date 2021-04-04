#!/usr/bin/env python3


def length(a, b, idx_a, idx_b, cache):
    if idx_a == 0 or idx_b == 0:
        return 0
    if cache[idx_a][idx_b] != 0:
        return cache[idx_a][idx_b]
    if a[idx_a - 1] == b[idx_b - 1]:
        cache[idx_a][idx_b] = length(a, b, idx_a - 1, idx_b - 1, cache) + 1
    else:
        cache[idx_a][idx_b] = max(
            length(a, b, idx_a, idx_b - 1, cache), length(a, b, idx_a - 1, idx_b, cache)
        )
    return cache[idx_a][idx_b]


def main():
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")
    cache = [[0 for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]
    print(length(first, second, len(first), len(second), cache))


if __name__ == "__main__":
    main()
