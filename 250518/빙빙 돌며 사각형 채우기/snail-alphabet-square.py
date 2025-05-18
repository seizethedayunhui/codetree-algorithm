# cht(int) -> 아스키 코드 변환
start_num = 65 # end = 90

N, M = map(int, input().split())

mat = [ [ "" for _ in range(M) ] for _ in range(N) ]

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

x, y = 0, 0
direc_num = 0

# 반복문 종료 조건으로 사용
cnt = 0

def in_range(x, y, N, M) :
    return ( 0 <= x < N ) and ( 0 <= y < M )

while True :

    if cnt >= N * M :
        break

    # Z 보다 커지면 다시 start_num이 A가 되도록 수정
    if start_num > 90 :
        start_num = 65

    mat[x][y] = chr(start_num)
    cnt += 1
    start_num += 1

    nx = x + dx[direc_num]
    ny = y + dy[direc_num]

    if not ( in_range(nx, ny, N, M) and not mat[nx][ny] != "") :
        """
            방향의 전환
            오른쪽 -> 아래쪽 0 1
            아래쪽 -> 왼쪽 1 2
            왼쪽 -> 위쪽 2 3
            위쪽 -> 오른쪽 3 0
        """
        # 방향의 전환
        direc_num = ( direc_num + 1 ) % 4

    x += dx[direc_num]
    y += dy[direc_num]

for row in mat :
    for col in row :
        print(col, end=" ")
    print()





    