from __future__ import annotations
from testgen import TestCollection, TestCase
from dataclasses import dataclass

MAXK = 60
MOD = int(1e9-63)

def solve(k: int) -> int:
    ans = 1
    for _ in range(k):
        ans *= ans * 16
        ans %= MOD
    return (ans * 6) % MOD


@dataclass
class RubiksTree(TestCase):
    k: int

    def validate(self) -> None:
        assert 1 <= self.k <= MAXK

    def write_input(self, input_f) -> None:
        print(self.k, file=input_f)
    
    def write_answer(self, answer_f, input_f) -> None:
        print(solve(self.k), file=answer_f)


tests = TestCollection('data/secret', RubiksTree)

for k in range(1, MAXK+1):
    def scope():
        scopek = k
        @tests.collect()
        def case() -> RubiksTree:
            return RubiksTree(scopek)
    scope()

if __name__ == '__main__':
    tests.generate()
