N = int(input())
mat = [list(map(int, input().split())) for _ in range(N) ]
dp = [ [ 1 for _ in range(N) ] for _ in range(N) ]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

ans = float('-inf')

for x in range(N):
    for y in range(N):

        for d1, d2 in zip(dx, dy):
            nx = x + d1
            ny = y + d2

            if in_range(nx, ny) and (mat[x][y] > mat[nx][ny]) :
                
                # dp 값이 초기값이 아닌 경우
                if dp[x][y] != 1 and dp[x][y] > dp[nx][ny]:
                    continue

                dp[x][y] = dp[nx][ny] + 1

        ans = max(ans, dp[x][y])

print(ans)

