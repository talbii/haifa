n, q = (int(x) for x in input().split())
p = [int(x) for x in input().split()]
p.sort()

s = [0] * (n + 1)
for i, v in enumerate(p, start=1):
    s[i] = s[i - 1] + v

for _ in range(q):
    x, y = (int(x) for x in input().split())
    print(s[n - x + y] - s[n - x])
