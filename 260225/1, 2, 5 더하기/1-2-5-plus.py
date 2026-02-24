N = int(input())

dp = [ 0 ] * (N+1)

for i in range(N+1):

    for e in [1, 2, 5]:

        if i - e > 0:
            dp[i] += dp[i-e]

        if i == e:
            dp[i] += 1

print(dp[N] % 10007)