N = int(input())

dp = [ -1 ] * (N+1)

dp[0] = 1
dp[1] = 2

for i in range(2, N+1):
    if i == 2 :
        dp[2] = 7
    else:
        dp[i] = dp[i-3] * 2 + dp[i-2] * 3 + dp[i-1] * 2

print(dp[N])