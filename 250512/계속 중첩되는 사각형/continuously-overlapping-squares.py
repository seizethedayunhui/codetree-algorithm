mat = [[ 0 for _ in range (2001)] for _ in range(2001)]

# 입력
N = int(input())

# 커맨드
commads = list()
for _ in range(N) :
    x1, y1, x2, y2 = map(int, input().split())
    command = [x1, y1, x2, y2]
    commads.append(command)


# 순서를 나누었을 때, % 2 가 1이면 파란색

current = 1000
for i in range(N) :

    if ( i % 2 ) :
        color = 2
    else :
        color = 1

    for x in range(commads[i][0], commads[i][2]) :
        for y in range(commads[i][1], commads[i][3]) :
            mat[current + x][current + y] = color


cnt = 0
for row in mat :
    for col in row :
        if col == 2 :
            cnt += 1

print(cnt)