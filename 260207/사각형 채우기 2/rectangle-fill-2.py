N = int(input())

dp = [ 0 ] * (N+1)
dp[0] = 1

for i in range(1, N+1):

    if i == 1:
        dp[i] = 1
    else :
        dp[i] = 2 * dp[i-2] + dp[i-1]

ans = dp[N] % 10007
print(ans)