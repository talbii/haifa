from __future__ import annotations
from dataclasses import dataclass
from typing import TextIO, TYPE_CHECKING

from testgen import TestCase, TestCollection

if TYPE_CHECKING:
    from random import Random

MAX_LEN = 10_000
VALID_CHARS = ('A', 'T', 'G', 'C')


@dataclass
class DNASequencing(TestCase):
    s: str

    def validate(self) -> None:
        assert isinstance(self.s, str)
        assert 1 <= len(self.s) <= MAX_LEN
        for char in self.s:
            assert char in VALID_CHARS

    def write_input(self, input_f: TextIO) -> None:
        print(len(self.s), self.s, file=input_f)


tests = TestCollection('data/secret', DNASequencing)


@tests.collect(params={'char': VALID_CHARS})
def same_char(char) -> DNASequencing:
    return DNASequencing(char * MAX_LEN)


@tests.collect(params={'pattern': (
    'ATGC', 'TGCA', 'GCAT', 'CATG', 'CGTA', 'ACTG', 'ACGT',
    'AT', 'AG', 'AC', 'CG', 'GC', 'CGT', 'TGC', 'AAC', 'CCCG',
)})
def repeating_pattern(pattern) -> DNASequencing:
    times = MAX_LEN // len(pattern)
    return DNASequencing(pattern * times)


@tests.collect(repeat=25)
def uniform_random(random: Random) -> DNASequencing:
    return DNASequencing(''.join(random.choices(tuple(VALID_CHARS), k=MAX_LEN)))


if __name__ == '__main__':
    tests.generate()
