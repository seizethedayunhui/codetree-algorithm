N = int(input())

N_list = list()

for _ in range(N) :

    l, char = input().split()
    l = int(l)

    N_list.append([l, char])

N_list.sort(lambda x : x[0])


max_dis =  0 if N == 1 else float('-inf')

for i in range(N) :

    G_cnt = 0
    H_cnt = 0

    current_char = N_list[i][1]
    start_char_idx = i
    same_char_dis = float('-inf')

    same_cnt_dis = float('-inf')


    for j in range(i, N) :

        if N_list[j][1] == "G" :
            G_cnt += 1

        if N_list[j][1] == "H" :
            H_cnt += 1
        
        # 계속 같은 문자만 이어지는 경우를 고려하여, ==을 조건으로 삼음(!= 대신에)
        if N_list[j][1] == current_char :
            
            # 같은 문자끼리 있는 구간의 길이
            current_char_dis = N_list[j][0] - N_list[start_char_idx][0]

            # 같은 문자끼리 있는 구간의 최대 크기만 저장
            same_char_dis = max(same_char_dis, current_char_dis)

        else :
            # 같은 문자인지 확인하기 위한 기록
            current_char = N_list[j][1]
            # 인덱스 갱신
            start_char_idx = j

        if G_cnt == H_cnt :

            current_cnt_dis = N_list[j][0] - N_list[i][0]
            same_cnt_dis = max(same_cnt_dis, current_cnt_dis)

    # print(same_char_dis, same_cnt_dis)
    if same_cnt_dis >= same_char_dis :
        max_dis = max(max_dis, same_cnt_dis)
    else :
        max_dis = max(max_dis, same_char_dis)

print(max_dis)





