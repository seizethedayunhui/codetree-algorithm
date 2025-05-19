# 입력받기
N = int(input())

# 시작 위치
x = N // 2
y = N // 2

# 격자판
mat = [ [ 0 for _ in range(N) ] for _ in range(N) ]
cnt = 1 # 기록할 숫자

# 범위 안에 있는지 확인하는 함수
def in_range(x, y, N) :
    return ( 0 <= x < N ) and ( 0 <= y < N )

# 방향 조정
dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

direc_num = 0
move_cnt = 1
repeat_cnt = 0
break_flag = False

while True :

    if break_flag :
        break


    if repeat_cnt == 2 :
        # print("반복조건 확인", repeat_cnt)
        repeat_cnt = 0
        move_cnt += 1

    # 두번 반복되지 않았고, N-1보다 작은 범위로 이동하는 경우
    if (move_cnt < N - 1) and (repeat_cnt < 2):

        for _ in range(move_cnt) :
            mat[x][y] = cnt
            cnt += 1

            # print("1번 반복문", move_cnt, x, y, mat[x][y])
            x += dx[direc_num]
            y += dy[direc_num]
        # print("반복의 종료")

        direc_num = ( direc_num + 3 ) % 4
        repeat_cnt += 1

    else :
        for _ in range(move_cnt) :

            mat[x][y] = cnt
            cnt += 1
            # print("2번 반복문", move_cnt, x, y, mat[x][y])
            x += dx[direc_num]
            y += dy[direc_num]

            if cnt > N * N :
                break_flag = True
                break

        # print("반복의 종료")

        direc_num = ( direc_num + 3 ) % 4


        
        
       
    

for row in mat :
    for elem in row :
        print(elem, end=" ")
    print()

    

    

