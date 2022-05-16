from __future__ import annotations
from dataclasses import dataclass
from subprocess import run

from testgen import TestCollection, TestCase

MAXN = 2500


@dataclass
class LasVegas(TestCase):
    probability: list[float]

    def write_input(self, input_f) -> None:
        print(len(self.probability), file=input_f)
        print(' '.join(str(p) for p in self.probability), file=input_f)

    def write_answer(self, answer_f, input_f) -> None:
        run('./accepted.out', stdout=answer_f, stdin=input_f)

    def validate(self) -> None:
        assert 1 <= len(self.probability) <= MAXN
        for p in self.probability:
            assert isinstance(p, float)
            assert 0 <= p <= 1


tests = TestCollection('data/secret', LasVegas)


@tests.collect(repeat=3)
def random_maxn(random) -> LasVegas:
    return LasVegas([
        random.randint(0, 100) / 100
        for _ in range(MAXN)
    ])


@tests.collect(repeat=5)
def random(random) -> LasVegas:
    return LasVegas([
        random.randint(0, 100) / 100
        for _ in range(random.randint(1, MAXN))
    ])


@tests.collect(repeat=10)
def random_short(random) -> LasVegas:
    return LasVegas([
        random.randint(0, 100) / 100
        for _ in range(random.randint(1, 20))
    ])


if __name__ == '__main__':
    tests.generate()
