N, M, r, c = map(int, input().split())

mat = [[ 0 for _ in range(N) ]  for _ in range(N) ]
temp = [[ 0 for _ in range(N) ]  for _ in range(N) ]
r -= 1
c -= 1

mat[r][c] = 1

dx = [ 0, 1, 0, -1]
dy = [ 1, 0, -1, 0]

def in_range(x, y) :
    return 0 <= x < N and 0 <= y < N

for t in range(M) :

    bomb_range = 2 ** (t)

    for x in range(N) :
        for y in range(N) :
            # 폭탄이 있는 경우 현재 초에 맞추어서 새로운 폭탄 bomb!
            if mat[x][y] :
                for i in range(4) :
                    nx = x + dx[i] * bomb_range
                    ny = y + dy[i] * bomb_range
                    if in_range(nx, ny) :
                        temp[nx][ny] = 1
    # 코드 복사
    for i in range(N) :
        for j in range(N) :
            if temp[i][j] :
                mat[i][j] = temp[i][j]

cnt = 0
for row in mat :
    for col in row :
        cnt += col

print(cnt)


                    