N = int(input())
arr = list(map(int, input().split()))
dp = [ 1 for _ in range(N) ]

for i in range(N):
    for j in range(i):

        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

ans = float('-inf')
for k in range(N):
    ans = max(ans, dp[k])

print(ans)