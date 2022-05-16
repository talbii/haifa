from __future__ import annotations
from testgen import TestCollection, TestCase
from dataclasses import dataclass
from subprocess import run
from queue import Queue

MAXN = int(2e5)


def parents_to_children(parents: list[int]) -> list[list[int]]:
    children = [list() for _ in range(len(parents))]
    for i, p in enumerate(parents):
        children[p].append(i)
    return children


def validate_tree(u: int, children: list[list[int]], seen: list[bool]):
    assert not seen[u]
    seen[u] = True
    for v in children[u]:
        validate_tree(v, children, seen)


@dataclass
class Parties(TestCase):
    b: list[int]

    def write_input(self, input_f) -> None:
        print(len(self.b) + 1, file=input_f)
        print(' '.join(str(bi) for bi in self.b), file=input_f)

    def write_answer(self, answer_f, input_f) -> None:
        process = run('./accepted.out', stdout=answer_f, stdin=input_f)
        assert process.returncode == 0

    def validator(self) -> None:
        n = len(self.b) + 1
        assert n <= MAXN
        for v in self.b:
            assert 1 <= v <= n

        tree = parents_to_children([0, 0] + self.b)
        seen = [False] * len(tree)
        validate_tree(1, tree, seen)
        for s in seen[2:]:
            assert s


tests = TestCollection('data/secret', Parties)


def generate_tree(
    n: int,
    direct_children_range: tuple[int, int],
    chance_no_children: float,
    random,
) -> list[int]:
    parents = [0] * (n + 1)
    avaliable = list(range(2, n + 1))
    random.shuffle(avaliable)
    queue = Queue()
    queue.put(1)

    while avaliable:
        if queue.empty():
            u = 1
        else:
            u = queue.get()

        if random.random() < chance_no_children:
            continue

        children = random.randint(*direct_children_range)
        for _ in range(children):
            if not avaliable:
                return parents
            v = avaliable.pop()
            parents[v] = u
            queue.put(v)

    return parents


@tests.collect(desc='n=1')
def single_worker() -> Parties:
    return Parties([])


@tests.collect(desc='1,2,3,... spaghetti tree, max n')
def spaghetti_ordered() -> Parties:
    return Parties(list(range(1, MAXN)))


@tests.collect(desc='spaghetti tree, random nodes order', repeat=2)
def random_spaghetti(random) -> Parties:
    avaliable = list(range(2, MAXN + 1))
    random.shuffle(avaliable)
    lst = [-1] * (MAXN + 1)

    lst[avaliable[0]] = 1
    for prev, cur in zip(avaliable[:-1], avaliable[1:]):
        lst[cur] = prev

    return Parties(lst[2:])


@tests.collect(desc='maxn children of root')
def all_root_children() -> Parties:
    return Parties([1] * (MAXN - 1))


@tests.collect(
    repeat=2,
    desc='random binary tree, 2 children on every node except leaves, max n',
)
def random_full_bintree(random) -> Parties:
    return Parties(generate_tree(
        n=MAXN,
        direct_children_range=(2, 2),
        chance_no_children=0,
        random=random,
    )[2:])


@tests.collect(
    repeat=3,
    desc='random tree, up to 100 children per node, 1/2 chance of no children',
)
def random_tree(random) -> Parties:
    return Parties(generate_tree(
        n=random.randint(10_000, 100_000),
        direct_children_range=(1, 100),
        chance_no_children=0.5,
        random=random,
    )[2:])


@tests.collect(
    repeat=10,
    desc='small tree, max of 3 children per node, high chance of no children',
)
def thin_random_tree(random) -> Parties:
    return Parties(
        generate_tree(
            n=random.randint(5_000, 10_000),
            direct_children_range=(0, 3),
            chance_no_children=0.75,
            random=random,
        )[2:]
    )


if __name__ == '__main__':
    tests.generate()
