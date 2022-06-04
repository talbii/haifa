def solve(i: int) -> bool:
    ans = False
    i -= 1
    while i > 0:
        if (i % 2 == 1):
             ans = not ans
        i //= 2
    return ans

t = int(input())
ns = (int(i) for i in input().split())
for n in ns:
    print(int(solve(n)), end='')
print()
