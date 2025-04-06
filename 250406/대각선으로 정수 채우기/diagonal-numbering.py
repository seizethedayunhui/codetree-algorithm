N, M = map(int, input().split())

# 새로운 배열
new_mat = [ [ 0 for _ in range(M) ] for _ in range(N) ]

# 범위 안에 있는지 확인하는 함수
def in_range(i, j) :
    return 0<= i < N and 0 <= j < M 

num = 1

# 열범위로 돌기
for col in range(M) :
    for row in range(N) :

        new_col = col - row

        if in_range(row, new_col) :
            new_mat[row][new_col] = num
            num += 1 # 값을 증가시켜줌
        else :
            break

# 행 범위로 돌기
for row in range(1, N) :
    for col in range(M-1, -1, -1) :
        if in_range(row, col) :
            new_mat[row][col] = num
            num += 1
            row += 1

        else :
            break
    
        

for i in range(N) :
    for j in range(M) :
        print(new_mat[i][j], end=" ")
    print()