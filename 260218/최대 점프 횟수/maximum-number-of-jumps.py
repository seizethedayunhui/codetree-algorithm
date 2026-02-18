N = int(input())
arr = list(map(int, input().split()))

min_value = float('-inf')
dp = [ min_value for _ in range(N) ]

dp[0] = 0
ans = float('-inf')
for i in range(N):
    for j in range(i):

        if j + arr[j] >= i and dp[j] != min_value:
            dp[i] = max(dp[i], dp[j]+1)
        
    ans = max(ans, dp[i])

print(ans)