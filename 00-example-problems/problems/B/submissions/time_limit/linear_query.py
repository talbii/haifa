n, q = (int(x) for x in input().split())
p = [int(x) for x in input().split()]
p.sort()
for _ in range(q):
    x, y = (int(x) for x in input().split())
    print(sum(p[n - x: n - x + y]))
