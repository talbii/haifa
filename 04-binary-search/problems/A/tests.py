from __future__ import annotations
from testgen import TestCollection, TestCase
from dataclasses import dataclass


MAXN = int(1e4)
MAXA = int(1e9)
HALF2 = MAXN // 2
HALF1 = MAXN - HALF2


@dataclass
class Ramon(TestCase):
    arr: list[int]

    def validate(self) -> None:
        assert 1 <= len(self.arr) <= MAXN
        for v in self.arr:
            assert 1 <= v <= MAXA
        for a, b in zip(self.arr[1:], self.arr[:-1]):
            assert a != b

    def write_input(self, input_f) -> None:
        print(len(self.arr), file=input_f)
        print(' '.join(str(v) for v in self.arr), file=input_f)


tests = TestCollection('data/secret', Ramon)


@tests.collect()
def pyramid() -> Ramon:
    first = list(range(1, HALF1 + 1))
    last = list(range(HALF1 - 1, 0, -1))
    return Ramon(first + last)


@tests.collect()
def hole() -> Ramon:
    first = list(range(HALF1, 0, -1))
    last = list(range(2, MAXN - HALF1))
    return Ramon(first + last)


@tests.collect()
def peak() -> Ramon:
    first = [HALF2 - i for i in range(HALF2)]
    last = [i for i in range(1, HALF1)]
    return Ramon(first + [MAXN] + last)


@tests.collect()
def single() -> Ramon:
    return Ramon([1])


@tests.collect()
def updown() -> Ramon:
    return Ramon([1, 2] * (MAXN // 2))


@tests.collect()
def upupdown() -> Ramon:
    return Ramon([1, 2, 3] * (MAXN // 3))


@tests.collect()
def up() -> Ramon:
    return Ramon(list(range(1, MAXN + 1)))


@tests.collect()
def down() -> Ramon:
    return Ramon(list(range(MAXN, 0, -1)))


@tests.collect(repeat=3)
def max_random(random) -> Ramon:
    return Ramon([random.randint(1, MAXA) for _ in range(MAXN)])


@tests.collect(repeat=10)
def random(random) -> Ramon:
    return Ramon([
        random.randint(1, MAXA)
        for _ in range(random.randint(1, 1_000))
    ])


@tests.collect(repeat=5)
def random_pit(random) -> Ramon:
    pit = random.randint(1, MAXN)
    first = list(range(pit, 0, -1))
    second = list(range(2, MAXN - pit + 2))
    return Ramon(first + second)


if __name__ == '__main__':
    tests.generate(3)
