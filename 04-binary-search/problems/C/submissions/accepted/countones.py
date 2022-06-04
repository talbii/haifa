def solve(i: int) -> int:
    return bin(i-1).count('1') % 2 != 0

t = int(input())
ns = (int(i) for i in input().split())
for n in ns:
    print(int(solve(n)), end='')
print()
