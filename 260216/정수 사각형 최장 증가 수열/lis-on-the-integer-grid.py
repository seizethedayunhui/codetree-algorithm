N = int(input())
mat = [list(map(int, input().split())) for _ in range(N) ]
dp = [ [ 1 for _ in range(N) ] for _ in range(N) ]
visited = [[ False for _ in range(N) ] for _ in range(N) ]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

ans = float('-inf')


def dfs(x, y, cnt):
    
    max_cnt = dp[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if in_range(nx, ny) and (mat[x][y] > mat[nx][ny]):

            if not visited[nx][ny]:
                dp[nx][ny] = dfs(nx, ny, dp[nx][ny] + 1)
                visited[nx][ny] = True

            max_cnt = max(max_cnt, dp[nx][ny]+1)
            dp[x][y] = max_cnt

    return max_cnt


for x in range(N):
    for y in range(N):

        for d1, d2 in zip(dx, dy):
            nx = x + d1
            ny = y + d2

            if in_range(nx, ny) and (mat[x][y] > mat[nx][ny]):

                if not visited[nx][ny]:
                    dp[nx][ny] = dfs(nx, ny, dp[nx][ny])
                    visited[nx][ny] = True

                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)

        ans = max(ans, dp[x][y])
        # print()
        # for i in range(N):
        #     for j in range(N):
        #         print(dp[i][j], end=" ")
        #     print()

print(ans)

