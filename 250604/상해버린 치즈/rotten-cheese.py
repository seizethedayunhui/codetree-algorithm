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
    for j in range(D) :
        if records[j]['m'] == i+1 :

            sick_flag = False
            for k in range(S) :
                # 아프다는 정보가 주어진 경우
                if sick_records[k]['p'] == records[j]['p'] and sick_records[k]['t'] > records[j]['t'] :
                    sick_flag = True
                    # print(records[j]['p'], 1)
                    cnt += 1
            # 아프다는 정보가 주어지지 않은 경우엔 아플 수도 있으니 추가해줌
            if not sick_flag :
                # print(records[j]['p'], 2)
                cnt += 1

    max_medicine = max(max_medicine, cnt)

    

print(max_medicine)

    