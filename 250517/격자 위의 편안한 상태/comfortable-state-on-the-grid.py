N, M = map(int, input().split())

mat = [ [ 0 for _ in range(N) ] for _ in range(N) ]

# 범위 벗어하는지 확인
def in_range(x, y, N) :
    return ( 0 <= x < N ) and ( 0 <= y < N )

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

for _ in range(M) :

    r, c = map(int, input().split())

    # 편안한 상태인지 확인하기 위한 변수 정의
    cnt = 0

    # x, y 정의
    x , y = r-1, c-1
    mat[x][y] += 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        # 만약, 범위 안이고 값이 1이라면 cnt 함
        if in_range(nx, ny, N) and mat[nx][ny] == 1 :
            cnt += 1

    if cnt == 3 :
        print(1)
    else :
        print(0)
