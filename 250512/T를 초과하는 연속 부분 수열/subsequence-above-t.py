N, T = map(int, input().split())

N_list = list(map(int, input().split()))

flag = False
max_len = float('-inf')

cnt = 1
for i in range(N) :

    # 일단 값이 T 보다 큰 경우에
    if N_list[i] > T :
        # flag값으로 연속으로 cnt 중인지를 체크 
        if flag :
            cnt += 1
        else :
            cnt = 1
            flag = True
    # 크지 않다면 flag를 False 로 변경
    else :
        flag = False

    if cnt > max_len :
        max_len = cnt

print(max_len)