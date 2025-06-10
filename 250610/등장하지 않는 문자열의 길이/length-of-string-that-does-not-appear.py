N = int(input())
string = [ elem for elem in input() ]
find_flag = False

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

        if current_cnt == 1 :
            find_flag = True
            min_len = (j - i)
            break
    if find_flag :
        break

print(min_len)


