import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [ False for _ in range(M)] for _ in range(N) ]

def in_range(x, y) :
    return 0 <= x < N and 0 <= y < M

def can_go(x, y, K) :
    return in_range(x, y) and mat[x][y] > K and not visited[x][y]

dx = [ 0, 1, 0 , -1]
dy = [ 1, 0, -1, 0]

def dfs(x, y, K) :

    visited[x][y] = True

    for i in range(4) :

        nx = x + dx[i]
        ny = y + dy[i]

        if can_go(nx, ny, K) :
            dfs(nx, ny, K)

max_cnt = float('-inf')
min_k = float('inf')

for k in range(1, 100):

    safe_section_cnt = 0

    for i in range(N) :
        for j in range(M) :
            if can_go(i, j, k) :
                dfs(i, j, k)
                safe_section_cnt += 1

    if max_cnt == safe_section_cnt :
        min_k = min(min_k, k)

    elif safe_section_cnt > max_cnt :
        max_cnt = safe_section_cnt
        min_k = k

    visited = [ [ False for _ in range(M)] for _ in range(N) ]

print(min_k, max_cnt)






