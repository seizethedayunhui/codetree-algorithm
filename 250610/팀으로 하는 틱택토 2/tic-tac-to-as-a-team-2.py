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
    digit_list = list()
    if flag :
        for idx, digit in enumerate(digits) :
            if digit :
                digit_cnt += 1
                digit_list.append(idx)

    return digit_cnt, digit_list

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
    digit_list = list()
    if flag :
        for idx, digit in enumerate(digits) :
            if digit :
                digit_cnt += 1
                digit_list.append(idx)

    return digit_cnt, digit_list

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
    digit_list = list()
    if flag :
        for idx, digit in enumerate(digits) :
            if digit :
                digit_cnt += 1
                digit_list.append(idx)

    return digit_cnt, digit_list

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
    digit_list = list()
    if flag :
        for idx, digit in enumerate(digits) :
            if digit :
                digit_cnt += 1
                digit_list.append(idx)

    return digit_cnt, digit_list 
    
            
cnt = 0
couples = list()
for i in range(3) :
    for j in range(3) :

        result1, couple1 = horizontal(i, j, mat) 
        result2, couple2 = vertical(i, j, mat) 
        result3, couple3 = diagonal1(i, j, mat)
        result4, couple4 = diagonal2(i, j, mat)

        results = [[result1, couple1], [result2, couple2], [result3, couple3], [result4, couple4]]

        for result in results :
            if result[0] == 2 and (result[1] not in couples) :
                cnt += 1
                couples.append(result[1])

        

print(cnt)
    

