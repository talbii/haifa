from __future__ import annotations

from testgen import TestCollection, TestCase
from dataclasses import dataclass
from subprocess import run

MAXN = int(2e5)
MAXA = int(1e9)


@dataclass
class Tabor(TestCase):
    points: list[int]

    def write_input(self, input_f) -> None:
        print(len(self.points), file=input_f)
        print(' '.join(str(p) for p in self.points), file=input_f)

    def write_answer(self, answer_f, input_f) -> None:
        run('./accepted.out', stdin=input_f, stdout=answer_f)

    def validate(self) -> None:
        assert 1 <= len(self.points) <= MAXN
        for p in self.points:
            assert 1 <= p <= MAXA


tests = TestCollection('data/secret', Tabor)


@tests.collect(desc='1,1,1,...')
def constant() -> Tabor:
    return Tabor([1] * MAXN)


@tests.collect(desc='1,2,3,...')
def ordered_up() -> Tabor:
    return Tabor(list(range(1, MAXN + 1)))


@tests.collect(desc='maxn,...,3,2,1')
def ordered_down() -> Tabor:
    return Tabor(list(range(MAXN, 0, -1)))


@tests.collect(desc='shuffled 1,2,3...')
def shuffled(random) -> Tabor:
    lst = list(range(1, MAXN + 1))
    random.shuffle(lst)
    return Tabor(lst)


@tests.collect(desc='max n random values', repeat=3)
def max_random(random) -> Tabor:
    return Tabor([random.randint(1, MAXA) for _ in range(MAXN)])


@tests.collect(desc='random values in [1,20], length is in [1,20]', repeat=5)
def short_random(random) -> Tabor:
    n = random.randint(1, 20)
    return Tabor([random.randint(1, 20) for _ in range(n)])


@tests.collect(desc='max length, max a_i in [1,20]', repeat=3)
def random_low_values(random) -> Tabor:
    return Tabor([random.randint(1, 20) for _ in range(MAXN)])


if __name__ == '__main__':
    tests.generate(4)
