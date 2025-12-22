N, M = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [ 0 for _ in range(M)] for _ in range(N) ]

def in_range(x, y) :
    return 0 <= x < N and 0 <= y < M 

def can_go(x, y) :
    return in_range(x, y) and not visited[x][y] and mat[x][y]

flag = 0

def dfs(x, y) :

    global flag

    if x == N-1 and y == M-1 :
        #print("들어왔어욥")
        flag = 1

    dx = [ 1, 0 ]
    dy = [ 0, 1 ]

    for i in range(2) :

        nx = x + dx[i]
        ny = y + dy[i]

        if can_go(nx, ny) :

            visited[nx][ny] = 1
            dfs(nx, ny)

dfs(0, 0)
print(flag)

