from __future__ import annotations
from timeit import repeat
from testgen import TestCollection, TestCase
from dataclasses import dataclass

MAXLEN = int(2e5)

@dataclass
class Basketball(TestCase):
    arr: list[int]

    def validate(self) -> None:
        lensum = 0
        for i in self.arr:
            assert 1 <= i
            lensum += len(str(i))
        assert lensum <= MAXLEN

    def write_input(self, input_f) -> None:
        print(len(self.arr), file=input_f)
        print(' '.join(str(v) for v in self.arr), file=input_f)

tests = TestCollection('data/secret', Basketball)


@tests.collect()
def increasing(random) -> Basketball:
    i = 1
    length = 0
    arr = list()

    while length <= MAXLEN:
        arr.append(i)
        length += len(str(i))
        i += 1
    
    arr.pop()
    random.shuffle(arr)
    return Basketball(arr)


@tests.collect()
def prime() -> Basketball:
    # 34790!-1 is a prime that consists of 142891 digits
    # https://primes.utm.edu/bios/code.php?code=p85
    
    from math import factorial
    return Basketball([factorial(34790)-1])


@tests.collect()
def random(random) -> Basketball:
    length = 0
    arr = list()

    while length <= MAXLEN:
        curlen = random.randint(1, 100)
        a = random.randint(1, 10 ** curlen)
        arr.append(a)
        length += len(str(a))
    
    arr.pop()
    return Basketball(arr)


@tests.collect()
def max_length() -> Basketball:
    return Basketball([int('9' * MAXLEN)])


if __name__ == '__main__':
    tests.generate(3)
