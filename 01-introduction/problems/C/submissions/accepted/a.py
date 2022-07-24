from fractions import Fraction
from math import inf


def maxdist(vi, vf, t, a):
    x = Fraction((a * t) + vf - vi, 2 * a)
    y = (a * x) + vi
    s1 = (vi + y) * Fraction(x, 2)
    s2 = (vf + y) * Fraction(t - x, 2)
    return s1 + s2


def mindist(vi, vf, t, a):
    x = Fraction((a * t) + vi - vf, 2 * a)
    y = -(a * x) + vi
    if y < 0:
        x1 = Fraction(vi, a)
        s1 = Fraction(vi * x1, 2)
        x2 = t - Fraction(vf, a)
        s2 = Fraction((t - x2) * vf, 2)
    else:
        s1 = (vi + y) * Fraction(x, 2)
        s2 = (vf + y) * Fraction(t - x, 2)
    return s1 + s2


n = int(input())
mi, ma = -inf, inf
for _ in range(n):
    vi, vf, t, a = (int(x) for x in input().split())
    ma = min(ma, maxdist(vi, vf, t, a))
    mi = max(mi, mindist(vi, vf, t, a))
print(*(float(x) for x in (mi, ma)))
