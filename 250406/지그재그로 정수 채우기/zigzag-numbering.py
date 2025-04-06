N, M = map(int, input().split())

new_mat = [ [ 0 for _ in range(M) ] for _ in range(N) ]

# 초기값은 0으로 설정
num = 0

# 열 기준으로 작성
# 짝수 열인 경우 -> 0행부터 시작
# 홀수 열인 경우 -> 마지막행부터 시작
for col in range(M) :
    # 홀수 열인 경우
    if col % 2 :
        for row in range(N-1, -1, -1) :
            new_mat[row][col] = num
            num += 1

    # 짝수 열인 경우
    else :
        for row in range(N) :
            new_mat[row][col] = num
            num += 1

for i in range(N) :
    for j in range(M) :
        print(new_mat[i][j], end=" ")
    print()
