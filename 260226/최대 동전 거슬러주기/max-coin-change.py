N, M = map(int, input().split())
MAX_VALUE = float('-inf')
coins = list(map(int, input().split()))

dp = [MAX_VALUE] * (M+1)
dp[0] = 0

for i in range(1, M+1):
    for j in range(N):
        if i >= coins[j]:
            dp[i] = max(dp[i], dp[i-coins[j]] + 1)

ans = dp[M]

if ans == MAX_VALUE:
    ans = -1
print(ans)