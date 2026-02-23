N, M = map(int, input().split())

coins = list(map(int, input().split()))

INT_MAX = float('inf')
dp = [ INT_MAX ] * (M+1)
dp[0] = 0

for i in range(1, M+1):
    for j in range(N):

        if i >= coins[j]:
            dp[i] = min(dp[i], dp[i-coins[j]] + 1)

ans = dp[M]
print(ans)