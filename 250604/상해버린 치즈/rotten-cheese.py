N, M, D, S = map(int, input().split())

records = list()

for _ in range(D) :

    p, m, t = map(int, input().split())

    record = dict()
    record['p'] = p
    record['m'] = m 
    record['t'] = t

    records.append(record)

sick_records = list()
for _ in range(S) :

    p, t = map(int, input().split())
    record = dict()

    record['p'] = p
    record['t'] = t

    sick_records.append(record)
    

max_medicine = float('-inf')

# 정확히 하나의 치즈가 상했다는 것. 
for i in range(M) :
    # i번의 치즈가 상했음
    # 각 사람들이 몇번째 치즈를 언제 먹었는지? >> 일단 선택된 치즈를 먹었는지 ? 그리고 먹었다면 아프기 전에 먹었는지
    cnt = 0
    eat_idx = list()

    for j in range(D) :
        # 상한 치즈를 먹은 경우
        if records[j]['m'] == i+1 :
            # 일단 아팠는지 여부는 알 수 없음.
            sick_flag = False
            # 이미 포함된 경우
            if records[j]['p'] in eat_idx :
                continue

            for k in range(S) :
                # 아프다는 정보가 주어진 경우
                if sick_records[k]['p'] == records[j]['p']  :

                    # 시간보다 이전에 아픈거면 cnt 되면 안되니까
                    sick_flag = True
                    if sick_records[k]['t'] > records[j]['t'] :
                        eat_idx.append(records[j]['p'])
                        # print("먹고 아팠음", records[j]['p'], 1)
                        cnt += 1
                        break
            # 아프다는 정보가 주어지지 않은 경우엔 아플 수도 있으니 추가해줌
            # 전에 아픈건데 추가될 수도 있음.
            if not sick_flag :
                # print("먹긴했지만, 아픈지는 안나와있음: ", records[j]['p'], 2)
                eat_idx.append(records[j]['p'])
                cnt += 1
    eat_idx.sort()
    #print(eat_idx)
   

    max_medicine = max(max_medicine, cnt)

    

print(max_medicine)

    