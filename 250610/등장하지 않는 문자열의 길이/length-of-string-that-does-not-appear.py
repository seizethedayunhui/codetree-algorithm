N = int(input())
string = [ elem for elem in input() ]

len_cnt = [ [ 0 for _ in range(N+1) ] for _ in range(N) ]

# 시작 위치 고정
for i in range(N) :
    # 길이 결정
    for j in range(i+1, N) :
        # 부분 문자열 결정
        partial = string[i:j]
        current_cnt = 0

        # 전체 범위에서 확인
        for k in range(N-i) :
            if string[k:k+(j-i)] == partial :
                current_cnt += 1

        # 카운트 처리 
        len_cnt[i][j-i] += current_cnt


for col in range(1, N+1) :

    flag = True
    for row in range(N) :
        if len_cnt[row][col] >= 2 :
            flag = False
            break
    # 찾았으면 바로 print
    if flag :
        print(col)
        break



