from collections import deque

N, K= map(int, input().split())

mat = [ list(map(int, input().split())) for _ in range(N) ]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

walls = list()
for i in range(N):
    for j in range(N):
        if mat[i][j]:
            walls.append((i, j))

dx = [ 0, 1, 0, -1 ] 
dy = [ 1, 0, -1, 0 ]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y, visited):
    return in_range(x, y) and not visited[x][y] and not mat[x][y]

def bfs(x, y):
    visited = [ [ False for _ in range(N) ] for _ in range(N) ]
    time = [ [ 0 for _ in range(N) ] for _ in range(N) ]

    final_time = -1

    q = deque()
    q.append((x,y))

    while q:

        cx, cy = q.popleft()
        ctime = time[cx][cy]

        if cx == r2 - 1 and cy == c2 - 1 :
            final_time = ctime
            break

        for d1, d2 in zip(dx, dy):
            nx = cx + d1
            ny = cy + d2

            if can_go(nx, ny, visited):
                q.append((nx, ny))
                time[nx][ny] = ctime + 1
                visited[nx][ny] = True

    return final_time

min_time = N*N + 1

def back_tracking(idx, cnt):

    global min_time

    if cnt == K:
        return bfs(r1-1, c1-1)
    
    if idx == len(walls):
        return min_time

    for w in range(idx, len(walls)):
        mat[walls[w][0]][walls[w][1]] = 0
        result = back_tracking(idx+1, cnt+1)

        if result != -1 :
            min_time = min(min_time, result)

        mat[walls[w][0]][walls[w][1]] = 1


    return min_time

ans = back_tracking(0, 0)

if ans == N*N+1:
    ans = -1
    
print(ans)

        

    



    