N, M = map(int, input().split())

# mat 정의
mat = [ [ 0 for _ in range(M)] for _ in range(N) ]

# 범위 체크 함수
def in_range(x, y, N, M) :
    return ( 0 <= x < N ) and ( 0 <= y < M ) 

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

# 시작 방향
dir_num = 0

# 시작 번호
cnt = 1
# 시작 위치
x = 0
y = 0

mat[x][y] = cnt

while True :

    if cnt >= N * M :
        break

    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    # 범위 먼저 확인
    # 범위 안에 없거나, 해당 위치에 이미 값이 차있을 경우 방향 전환
    if not in_range(nx, ny, N, M) or mat[nx][ny] != 0:
       
        dir_num = ( dir_num + 1 ) % 4
    
    cnt += 1
    x += dx[dir_num]
    y += dy[dir_num] 

    mat[x][y] = cnt

for row in mat :
    for col in row :
        print(col, end=" ")
    print()
  
        
        





