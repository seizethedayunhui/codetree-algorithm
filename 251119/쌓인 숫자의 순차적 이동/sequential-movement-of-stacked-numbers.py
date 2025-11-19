N, M = map(int, input().split())

# 가장 큰 값 계산하는 배열
mat = [ [ 0 for _ in range(N)] for _ in range(N)]
# 각 행, 열 속 원소 저장하는 배열
ans = [ [ [] for _ in range(N)] for _ in range(N)]
# 각 숫자들의 위치 저장하는 배열
points = [ [0, 0] for _ in range(N*N) ]

for x in range(N) :
    elements = list(map(int, input().split()))
    for y in range(N) :
        mat[x][y] = elements[y]
        ans[x][y] = [elements[y]]
        points[elements[y]-1] = [x, y]

dx = [ 0 , 1, 0, -1, -1, 1, -1, 1]
dy = [ 1, 0, -1, 0, 1, 1, -1, -1]

nums = list(map(int, input().split()))

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for num in nums :

    x = points[num-1][0]
    y = points[num-1][1]

    maxElement = 0
    nx, ny = x,y

    find_flag = False
    for i in range(8) :
        nx = x + dx[i]
        ny = y + dy[i]

        if in_range(nx, ny) and mat[nx][ny] > maxElement and mat[nx][ny] > 0:
            cx = nx
            cy = ny
            maxElement = mat[nx][ny]
            find_flag = True

    if not find_flag :
        continue

    # 숫자의 이동
    flag = False
    for k in range(len(ans[x][y])) :

        e = ans[x][y][k]

        if e == num :
            idx = k
            flag = True

        if flag :
            points[e-1] = [cx, cy]  

    ans[cx][cy] = ans[cx][cy] + ans[x][y][idx:]
    ans[x][y] = ans[x][y][:idx]   

    mat[cx][cy] = sorted(ans[cx][cy], reverse = True)[0]

    if len(ans[x][y]) >= 1 :
        mat[x][cy] = sorted(ans[x][y], reverse = True)[0]
    else :
        mat[x][y] = -1


for row in ans :
    for col in row :
        col.reverse()
        if len(col) >= 1 :
            print(*col)
        else :
            print(None)
        


            




