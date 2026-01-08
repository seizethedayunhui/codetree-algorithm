from collections import deque

x_q = deque()
y_q = deque()

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ] 

N, M = map(int, input().split())

visited = [ [ False for _ in range(M) ] for _ in range(N) ]

mat = [ list(map(int, input().split())) for _ in range(N) ]

def in_range(x, y) :
    return 0 <= x < N and 0 <= y < N

def can_go(x, y) :
    return in_range(x, y) and mat[x][y] and not visited[x][y]

def bfs(x, y) :

    x_q.append(x)
    y_q.append(y)

    visited[x][y] = True

    while x_q and y_q :

        x = x_q.popleft()
        y = y_q.popleft()

        if x == N-1 and y == M-1 :
            return 1
        
        for i in range(4) :

            nx = x + dx[i]
            ny = y + dy[i]

            if can_go(nx, ny) :
                visited[nx][ny] = True
                x_q.append(nx)
                y_q.append(ny)

    return 0

print(bfs(0, 0))


