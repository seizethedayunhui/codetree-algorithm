N, M = map(int, input().split())

mat = [ list(map(int, input().split())) for _ in range(N) ]
temp = [ [ element for element in row ] for row in mat ]
cols = [ int(input()) for _ in range(M) ]

dx = [ 0, 1, 0, -1]
dy = [ 1, 0, -1, 0]

def in_range(x, y) :
    return 0 <= x < N and 0 <= y < N

for col in cols :

    flag = False

    for row in range(N) :
        if mat[row][col - 1] :
            flag = True
            r = row
            c = col - 1
            break
    
    if flag :
        # 폭탄 터지기
        temp[r][c] = 0
        for i in range(4) :
            nx, ny = r, c
            for _ in range(mat[r][c]-1):
                nx += dx[i]
                ny += dy[i]

                if (in_range(nx, ny)) :
                    temp[nx][ny] = 0
        
        # 중력 작용
        for y in range(N) :
            x_idx = 0
            for x in range(N-1, -1, -1) :
                if not temp[x][y] :
                    x_idx = x
                
                if x_idx and temp[x][y] :
                    temp[x_idx][y] = temp[x][y]
                    temp[x][y] = 0
                    x_idx = x

        mat = [ [ element for element in row ] for row in temp ]

for x in range(N) :
    for y in range(N) :
        print(mat[x][y], end=" ")
    print()
        

