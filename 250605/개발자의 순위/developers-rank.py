K, N = map(int, input().split())

scores = list()

for _ in range(K) :

    score = list(map(int, input().split()))

    scores.append(score)

cnt = 0
for i in range(N) :
    for j in range(N) :
        if (i == j) :
            continue
        
        flag = True
        for k in range(K) :
            for l in range(N) :

                if scores[k][l] == (i+1) :
                    a_idx = l

                if scores[k][l] == (j+1) :
                    b_idx = l
            # 조건을 벗어나는 경우 flag를 False로 설정
            if a_idx > b_idx :
                flag = False
            # flag = Flase 인 경우 모든 경우 만족하지 않는다는 것이기 때문에 break
            if not flag :
                break
        # 모든 경우에 대해 flag가 True인 경우만 cnt += 1
        if flag :
            cnt += 1

print(cnt)
                

