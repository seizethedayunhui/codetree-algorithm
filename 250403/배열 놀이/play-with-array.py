N, Q = map(int, input().split())
N_arr = list(map(int, input().split()))
Q_arr = [list(map(int, input().split())) for _ in range(Q) ]


for q in Q_arr :
    if q[0] == 1 :
        print(N_arr[q[1]-1])
    elif q[0] == 2 :
        flag = 0 # 해당하는 원소가 있는지 확인함. 
        for i in range(N) :
            if N_arr[i] == q[1] :
                flag = 1
                print(i+1)
                break
        if not flag :
            print(0)
    else :
        # 슬라이싱할 때 인덱스 주의
        ans_arr = N_arr[q[1]-1:q[2]]
        for ans in ans_arr :
            print(ans, end=" ")
        print()
        

    