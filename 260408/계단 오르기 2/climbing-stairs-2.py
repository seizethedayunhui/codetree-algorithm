n = int(input())
arr = list(map(int, input().split()))
arr = [ 0 ] + arr
MIN_VALUE = float('-inf')
dp = [[ MIN_VALUE for _ in range(4) ] for _ in range(n+1) ]

dp[0][0] = 0
dp[1][1] = arr[1]

for i in range(2, n+1):
    for j in range(4):

        if j == 0:
            if dp[i-2][j] != MIN_VALUE:
                dp[i][j] = dp[i-2][j] + arr[i]
        else:
            dp[i][j] = max(dp[i-2][j], dp[i-1][j-1]) + arr[i]

answer = MIN_VALUE

for k in range(4):
    answer = max(answer, dp[n][k])

print(answer)
            