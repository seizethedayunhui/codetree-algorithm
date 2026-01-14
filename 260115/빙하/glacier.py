from collections import deque

N, M = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [ False for _ in range(M)] for _ in range(N) ]

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

q = deque()

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    return in_range(x, y) and mat[x][y] and not vistied[x][y]

def initial_q():
    
    all_ice = 0

    for x in range(N):
        for y in range(M):

            all_ice += mat[x][y]

            if mat[x][y] == 0:
                ice = 0
                not_visited = 0
                for i in range(4):

                    nx = x + dx[i]
                    ny = y + dy[i]

                    if in_range(nx, ny) and mat[nx][ny] :

                        ice += mat[nx][ny]

                        if not visited[nx][ny]:
                            not_visited += 1
                            q.append((nx, ny))
                            visited[nx][ny] = True
                if ice == 4:
                    for _ in range(not_visited):
                        cx, cy = q.pop()
                        visited[cx][cy] = False
    # for i in range(N):
    #     for j in range(M):
    #         print(visited[i][j], end=" ")
    #     print()
    return all_ice

def ice_breaking(q):

    next_q = q.copy()
    current_ice = len(next_q)
    second = 0

    while next_q:

        current_ice = len(next_q)
        second += 1
        next_q = deque()
    
        while q:
            x, y = q.popleft()
            #print(x, y)

            ice = 0
            not_visited = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if in_range(nx, ny) and mat[nx][ny] :

                    ice += 1

                    if not visited[nx][ny]:
                        #print("추가", nx, ny)
                        next_q.append((nx, ny))
                        not_visited += 1
                        visited[nx][ny] = True

            if ice == 4:
                for _ in range(not_visited):
                    cx, cy = next_q.pop()
                    visited[cx][cy] = False

        q = next_q.copy()   
        #print(len(next_q))

    return second, current_ice

initial_ice = initial_q()
ans1, ans2 = ice_breaking(q)
print(ans1, ans2)






