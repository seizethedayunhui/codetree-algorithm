N, M = map(int, input().split())

mat = [ [ 0 for _ in range(M) ] for _ in range(N) ]

cnt = 1

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

direc_num = 1
x, y = 0, 0

# 범위 체크
def in_range(x, y, N, M) :
    return ( 0 <= x < N ) and ( 0 <= y < M )

while True:
    # 다 채운 경우 break
    if cnt > N * M :
        break

    mat[x][y] = cnt
    cnt += 1

    # 다음 차례
    nx = x + dx[direc_num]
    ny = y + dy[direc_num]

    # 범위를 벗어나는 경우 방향을 전환 
    if not (in_range(nx, ny, N, M) and  not mat[nx][ny]) :
        """
            아래 -> 오른쪽 1 0
            오른쪽 -> 위로 0 3
            위로 -> 왼쪽 3 2
            왼쪽 -> 아래 2 1
        """
        direc_num = ( direc_num + 3 ) % 4

    x += dx[direc_num]
    y += dy[direc_num]

for row in mat:
    for col in row :
        print(col, end=" ")
    print()




    
