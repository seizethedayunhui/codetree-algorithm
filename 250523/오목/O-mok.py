N = 19
mat = list()

for _ in range(19) :
    row = list(map(int, input().split()))
    mat.append(row)

# 함수를 만든다. -> 행, 열, 대각선 별로
def in_range(x, y, N) :
    return ( 0 <= x < N ) and ( 0 <= y < N )

def is_win_in_row(x, y, mat) :

    dx = [1, 2, 3, 4]

    for i in range(4) :
        nx = x + dx[i]
        ny = y

        # 조건을 만족하지 않으면 바로 return
        if not(in_range(nx, ny, N) and mat[nx][ny] == mat[x][y]) :
            return False

    return True

def is_win_in_col(x, y, mat) :

    dy = [1, 2, 3, 4]

    for j in range(4) :
        nx = x
        ny = y + dy[j]

        if not(in_range(nx, ny, N) and mat[nx][ny] == mat[x][y]) :
            return False
    
    return True

def is_win_in_diagonal1(x, y, mat) :

    dx = [ 1, 2, 3, 4 ]
    dy = [ 1, 2, 3, 4 ]

    for k in range(4) :
        nx = x + dx[k]
        ny = y + dy[k]

        if not(in_range(nx, ny, N) and mat[nx][ny] == mat[x][y]) :
            return False

    return True

def is_win_in_diagonal2(x, y, mat) :

    dx = [ -1, -2, -3, -4 ]
    dy = [ 1, 2, 3, 4 ]

    for k in range(4) :
        nx = x + dx[k]
        ny = y + dy[k]

        if not(in_range(nx, ny, N) and mat[nx][ny] == mat[x][y]) :
            return False

    return True

ans_x, ans_y = 0, 0
black_win = False
white_win = False
nobody_win = True

for x in range(N) :
    for y in range(N) :

        if (mat[x][y] > 0):
            # 세로로 이긴 경우
            if is_win_in_row(x, y, mat) :
                ans_x = ( 2 * x + 4 ) // 2
                ans_y = y

            # 가로로 이긴 경우 
            elif is_win_in_col(x, y, mat) :
                ans_x = x
                ans_y = ( 2 * y + 4 ) // 2

            # 대각선으로 이긴 경우 1
            elif is_win_in_diagonal1(x, y, mat) :
                ans_x = ( 2 * x + 4 ) // 2
                ans_y = ( 2 * y + 4 ) // 2

            # 대각선으로 이긴 경우 2
            elif is_win_in_diagonal2(x, y, mat) :
                ans_x = ( 2 * x - 4 ) // 2
                ans_y = ( 2 * y + 4 ) // 2

            else :
                continue

            if mat[x][y] == 1 :
                black_win = True
                nobody_win = False
            
            if mat[x][y] == 2 :
                white_win = True
                nobody_win = False

            ans_x += 1
            ans_y += 1



if not nobody_win :
    if black_win :
        print(1)
    elif white_win :
        print(2)
    print(ans_x, ans_y)
else :
    print(0)


    
