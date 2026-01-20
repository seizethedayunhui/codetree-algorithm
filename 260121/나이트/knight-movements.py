from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

visited = [ [ False for _ in range(N) ] for _ in range(N) ]
step = [ [ 0 for _ in range(N) ] for _ in range(N) ]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y):
    return in_range(x, y) and not visited[x][y]

q = deque()

def push(x, y, prev_step):
    q.append((x, y))
    visited[x][y] = True
    step[x][y] = prev_step + 1

dx = [ -2, -1, 1, 2, 2, 1, -2, -1 ]
dy = [ 1, 2, 2, 1, -1, -2, -1, -2 ]

def reach_final(x, y):
    
    q.append((x-1, y-1))
    path = -1

    while q:
        x, y = q.popleft()
        prev_step = step[x][y] 

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if can_go(nx, ny):
                push(nx, ny, prev_step)

                if nx == r2-1 and ny == c2-1:
                    path = step[nx][ny]
                    break

    return path

ans = reach_final(r1, c1)
print(ans)

