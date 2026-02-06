N = int(input())

mat = [ list(map(int, input().split())) for _ in range(N) ]
dp = [ [ 0 for _ in range(N) ] for _ in range(N) ]

dp[0][N-1] = mat[0][N-1]

# 오른쪽에서만 올 수 있는 것들 초기화
for col in range(N-2, -1, -1):
    dp[0][col] = dp[0][col + 1] + mat[0][col]

# 위에서만 올 수 있는 것들 초기화
for row in range(1, N):
    dp[row][N-1] = dp[row-1][N-1] + mat[row][N-1]

for i in range(1, N):
    for j in range(N-2, -1, -1):
        dp[i][j] = min(dp[i-1][j], dp[i][j+1]) + mat[i][j]

print(dp[N-1][0])