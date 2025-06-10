mat = [ [ int(elem) for elem in input() ] for _ in range(3) ]

def in_range(x, y) :
    return 0 <= x < 3 and 0 <= y < 3

# 가로
def horizontal(x, y, mat) :

    dx = [0, 1, 2]

    digits = [ 0 for _ in range(10) ]
    flag = True

    for i in range(3) :
        nx, ny = x + dx[i], y
        if in_range(nx, ny) :
            digits[mat[nx][ny]] += 1
        else :
            flag = False
            break

    digit_cnt = 0
    if flag :
        for digit in digits :
            if digit :
                digit_cnt += 1

    return digit_cnt

# 세로
def vertical(x, y, mat) :

    dy = [0, 1, 2]

    digits = [ 0 for _ in range(10) ]
    flag = True

    for i in range(3) :
        nx, ny = x , y + dy[i]
        if in_range(nx, ny) :
            digits[mat[nx][ny]] += 1
        else :
            flag = False
            break

    digit_cnt = 0
    if flag :
        for digit in digits :
            if digit :
                digit_cnt += 1

    return digit_cnt

# 대각선
def diagonal1(x, y, mat) :

    dx = [0, 1, 2]
    dy = [0, 1, 2]

    digits = [ 0 for _ in range(10) ]
    flag = True

    for i in range(3) :
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) :
            digits[mat[nx][ny]] += 1
        else :
            flag = False
            break

    digit_cnt = 0
    if flag :
        for digit in digits :
            if digit :
                digit_cnt += 1

    return digit_cnt

def diagonal2(x, y, mat) :

    dx = [0, 1, 2]
    dy = [0, -1, -2]

    digits = [ 0 for _ in range(10) ]
    flag = True

    for i in range(3) :
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) :
            digits[mat[nx][ny]] += 1
        else :
            flag = False
            break

    digit_cnt = 0
    if flag :
        for digit in digits :
            if digit :
                digit_cnt += 1

    return digit_cnt      
            
cnt = 0
for i in range(3) :
    for j in range(3) :
        if horizontal(i, j, mat) == 2 or vertical(i, j, mat) == 2 or diagonal1(i, j, mat) == 2 or diagonal2(i, j, mat) == 2:
            cnt += 1

print(cnt)
    

