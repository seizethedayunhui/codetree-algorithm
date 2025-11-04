N, M, Q = map(int, input().split())

mat = [ list(map(int, input().split())) for _ in range(N) ] # 아파트 정보
winds = [ list(input().split()) for _ in range(Q) ] # 바람정보

#  범위만 확인
def in_range(x) :
    return 0 <= x < N

# 열에 같은 숫자가 있는지 확인
def check_col(current_row, next_row) :

    flag = False
    for i in range(M) :
        # 같은게 있는 경우 True
        if (mat[current_row][i] == mat[next_row][i]) :
            flag = True
    return flag
    

# 바람 불기
def wind_func(direc, row, flag1, flag2) :

    if direc == "R" :
        temp = mat[row][0]
        for i in range(M-1) :
            mat[row][i] = mat[row][i+1]
        mat[row][M-1] = temp

    else :
        temp = mat[row][M-1]
        for i in range(M-1, 0, -1) :
            mat[row][i] = mat[row][i-1]
        mat[row][0] = temp
    
    # print("하나의 작은 바람이 지났습니다. ")
    # for x in range(N) :
    #     for y in range(M) :
    #         print(mat[x][y], end=" ")
    #     print()
    # print()

    # 다음 방향 진행을 위해 방뱡 교체
    if direc == "L" :
        direc = "R"
    else :
        direc = "L"
    
    # 범위 확인 && 조건 확인
    # 위 방향
    if (in_range(row-1) and check_col(row, row-1) and flag1) :
        # 방향 - flag1은 위쪽 진행
        # print("위쪽으로 진행합니다. ", row, in_range(row-1), check_col(row, row-1))
        wind_func(direc, row-1, flag1, False)

    if (in_range(row+1) and check_col(row, row+1) and flag2) :
        # 방향 - flag2는 아래쪽 진행
        # print("아래쪽으로 진행합니다. ", row, in_range(row+1), check_col(row, row+1))
        wind_func(direc, row+1, False, flag2)


# 바람은 하나가 불고 이후에 전파됨
for wind in winds :

    row = int(wind[0]) - 1
    direc = wind[1]

    wind_func(direc, row, True, True)

    # print("하나의 큰 바람이 지났습니다.")
    # for x in range(N) :
    #     for y in range(M) :
    #         print(mat[x][y], end=" ")
    #     print()   

    
for x in range(N) :
    for y in range(M) :
        print(mat[x][y], end=" ")
    print()



    

