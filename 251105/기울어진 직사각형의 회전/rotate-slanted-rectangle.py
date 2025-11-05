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

# 시계 방향
if direc :

    # 1번 방향
    currentX = pointX[1]
    currentY = pointY[1]

    for _ in range(moving[3]) :
        temp[currentX][currentY] = mat[currentX+1][currentY+1]
        currentX += 1
        currentY += 1
    # 1번 이동 후엔 갱신하지 않음

    # 2번 방향 이동
    currentX = pointX[2]
    currentY = pointY[2]
    for _ in range(moving[2]-1) :
        temp[currentX][currentY] = mat[currentX+1][currentY-1]
        currentX += 1
        currentY -= 1
    
    # 첫번쨰 갱신
    temp[currentX][currentY] = mat[pointX[1]][pointY[1]]
    # print(currentX, currentY, pointX[3], pointY[3], mat[pointX[3]][pointY[3]])

    # 3번 방향 이동
    currentX = pointX[3]
    currentY = pointY[3]
    for _ in range(moving[1]-1) :
        temp[currentX][currentY] = mat[currentX-1][currentY-1]
        currentX -= 1
        currentY -= 1
    
    # 두번째 갱신
    temp[currentX][currentY] = mat[pointX[2]][pointY[2]]

    # 4번 방향 이동
    currentX = pointX[0]
    currentY = pointY[0]
    for _ in range(moving[0]-1) :
        temp[currentX][currentY] = mat[currentX-1][currentY+1]
        currentX -= 1
        currentY += 1
    
    # 세번째 갱신
    temp[currentX][currentY] = mat[pointX[3]][pointY[3]]

# 반시계 방향
else :

    # 1번 방향
    currentX = pointX[1]
    currentY = pointY[1]

    for _ in range(moving[0]) :
        temp[currentX][currentY] = mat[currentX+1][currentY-1]
        currentX += 1
        currentY -= 1
    # 1번 이동 후엔 갱신하지 않음

    # 2번 방향 이동
    currentX = pointX[2]
    currentY = pointY[2]
    for _ in range(moving[1]-1) :
        temp[currentX][currentY] = mat[currentX+1][currentY+1]
        currentX += 1
        currentY += 1
    
    # 첫번쨰 갱신
    temp[currentX][currentY] = mat[pointX[1]][pointY[1]]
    # print(currentX, currentY, pointX[1], pointY[1], mat[pointX[1]][pointY[1]])

    # 3번 방향 이동
    currentX = pointX[3]
    currentY = pointY[3]
    for _ in range(moving[2]-1) :
        temp[currentX][currentY] = mat[currentX-1][currentY+1]
        currentX -= 1
        currentY += 1
    
    # 두번째 갱신
    temp[currentX][currentY] = mat[pointX[2]][pointY[2]]

    # 4번 방향 이동
    currentX = pointX[0]
    currentY = pointY[0]
    for _ in range(moving[3]-1) :
        temp[currentX][currentY] = mat[currentX-1][currentY-1]
        currentX -= 1
        currentY -= 1
    
    # 세번째 갱신
    temp[currentX][currentY] = mat[pointX[3]][pointY[3]]

# temp 값을 mat에 복사
for x in range(N) :
    for y in range(N) :
        mat[x][y] = temp[x][y]

for row in mat :
    for col in row :
        print(col, end= " ")
    print()