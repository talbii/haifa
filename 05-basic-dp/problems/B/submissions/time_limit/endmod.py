k = int(input())
n = (2 ** k) - 1
r = 6 * (4 ** (n - 1))
print(r % ((10 ** 9) - 63))
