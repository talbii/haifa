from __future__ import annotations
from math import floor, sqrt
from testgen import TestCase, TestCollection
from dataclasses import dataclass
from typing import TextIO

MAXN = int(2e5)
MAXQ = int(2e5)
MAXV = int(1e6)


@dataclass
class Promotion(TestCase):
    p: list[int]
    queries: list[tuple[int, int]]

    @property
    def n(self) -> int:
        return len(self.p)

    @property
    def q(self) -> int:
        return len(self.queries)

    def validate(self) -> None:
        assert 1 <= self.n <= MAXN
        for v in self.p:
            assert isinstance(v, int)
            assert 1 <= v <= MAXV

        assert 1 <= self.q <= MAXQ
        for x, y in self.queries:
            assert 1 <= y <= x <= self.n

    def write_input(self, input_f: TextIO) -> None:
        print(self.n, self.q, file=input_f)
        print(*self.p, file=input_f)
        for x, y in self.queries:
            print(x, y, file=input_f)

    def solve(self) -> list[int]:
        p = sorted(self.p)
        s = [0] * (self.n + 1)
        for i, v in enumerate(p, start=1):
            s[i] = s[i - 1] + v
        return [s[self.n - x + y] - s[self.n - x] for x, y in self.queries]

    def write_answer(self, answer_f: TextIO, input_f: TextIO) -> None:
        for v in self.solve():
            print(v, file=answer_f)


tests = TestCollection('data/secret', Promotion)


@tests.collect(repeat=10)
def all_possible_queries(random) -> Promotion:
    n = floor(sqrt(MAXQ)) - 5
    p = [random.randint(1, MAXV) for _ in range(n)]
    queries = [
        (x, y)
        for y in range(1, n + 1)
        for x in range(y, n + 1)
    ]
    random.shuffle(queries)
    return Promotion(p, queries)


@tests.collect(repeat=3)
def completely_random(random) -> Promotion:
    p = [random.randint(1, MAXV) for _ in range(MAXN)]
    queries = list()
    for _ in range(MAXQ):
        x, y = random.randint(1, MAXN), random.randint(1, MAXN)
        if x < y: x, y = y, x
        queries.append((x, y))
    return Promotion(p, queries)


@tests.collect(repeat=3)
def large_queries(random) -> Promotion:
    p = [random.randint(1, MAXV) for _ in range(MAXN)]
    queries = list()
    for _ in range(MAXQ):
        x = random.randint(floor((9 / 10) * MAXN), MAXN)
        y = random.randint(floor((9 / 10) * x), x)
        queries.append((x, y))
    return Promotion(p, queries)


if __name__ == '__main__':
    tests.generate()
