n = int(input())
arr = list(map(int, input().split()))

dp = [ float('-inf') for _ in range(n+1) ]

dp[1] = arr[0]

for i in range(2, n+1):
    dp[i] = max(dp[i-1] + arr[i-1], arr[i-1])

answer = float('-inf')
for j in range(n+1):
    answer = max(answer, dp[j])

print(answer)
