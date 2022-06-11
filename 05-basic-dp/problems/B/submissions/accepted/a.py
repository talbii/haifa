MOD = int(1e9-63)
k = int(input())
ans = 1
for i in range(2, k+1):
    ans *= ans * 16
    ans %= MOD
ans *= 6
print(ans % MOD)
