from collections import deque

N, M = map(int, input().split())

mat = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [ False for _ in range(M) ] for _ in range(N) ]
step = [ [ 0 for _ in range(M) ] for _ in range(N) ]

q = deque()
dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    return in_range(x, y) and mat[x][y] and not visited[x][y]

def push(x, y, current_path):
    q.append((x, y))
    step[x][y] = current_path + 1
    visited[x][y] = True 

def find_exit(x, y):
    q.append((x, y))
    path = -1

    while q:
        x, y = q.popleft()
        current_path = step[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if can_go(nx, ny):
                push(nx, ny, current_path)

                if nx == N-1 and ny == M-1:
                    path = step[nx][ny]
                    break
    return path

ans = find_exit(0, 0)
print(ans)

