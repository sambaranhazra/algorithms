#!/usr/bin/env python3

import collections
import math

Card = collections.namedtuple("Card", ["rank", "suite"])


class FrenchDeck:
    ranks = [str(n) for n in range(1, 11)] + list("JKQA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, multiplier):
        return Vector(self.x * multiplier, self.y * multiplier)

    def __rmul__(self, multiplier):
        return Vector(self.x * multiplier, self.y * multiplier)


if __name__ == "__main__":
    v = Vector(2, 3)
    print(v)
    print(10 * v)
    print(bool(Vector()))
