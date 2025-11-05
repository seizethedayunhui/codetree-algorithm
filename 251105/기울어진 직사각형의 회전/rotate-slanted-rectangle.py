N = int(input())
mat = [ list(map(int, input().split())) for _ in range(N) ]
temp = [ [ 0 for _ in range(N) ]  for _ in range(N) ]

for i in range(N) :
    for j in range(N) :
        temp[i][j] = mat[i][j]

move = list(map(int, input().split()))

x = move[0] - 1
y = move[1] - 1
moving = move[2:6]
direc = move[6]

if direc :
    dx = [ -1, -1, 1,  1]
    dy = [ -1,  1, 1, -1]
    order = [3, 2, 1, 0]
else :
    dx = [ -1 , -1, 1, 1]
    dy = [  1,  -1,-1, 1]
    order = [0, 1, 2, 3]

# 꼭짓점 저장
pointX = [x]
pointY = [y]

# 시작 위치
currentX = x 
currentY = y

for i in range(3) :
    currentX += dx[i] * moving[order[i]]
    currentY += dy[i] * moving[order[i]]
    pointX.append(currentX)
    pointY.append(currentY)

for i in range(4) :

    point_idx = (i+1) % 4

    currentX = pointX[point_idx]
    currentY = pointY[point_idx]

    d_idx = (point_idx + 1) % 4

    temp_idx = (point_idx + 3) % 4

    for _ in range(moving[order[i]]-1) :

        nx = currentX + dx[d_idx]
        ny = currentY + dy[d_idx]

        temp[currentX][currentY] = mat[nx][ny]
        
        currentX = nx
        currentY = ny

    temp[currentX][currentY] = mat[pointX[temp_idx]][pointY[temp_idx]]


# temp 값을 mat에 복사
for x in range(N) :
    for y in range(N) :
        mat[x][y] = temp[x][y]

for row in mat :
    for col in row :
        print(col, end= " ")
    print()
