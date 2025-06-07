N, B = map(int, input().split())

records = list()

for _ in range(N) :

    record = tuple(map(int, input().split()))
    records.append(record)

max_cnt = float('-inf')
for i in range(N) :

    price_sum = 0
    cnt = 0

    for j in range(N) :

        # 할인 받는 경우의 수
        if i == j :
            price_sum += (records[j][0] // 2)
        else :
            price_sum += records[j][0]

        price_sum += records[j][1]

        # 예산에 벗어난 경우 그냥 break
        if B - price_sum < 0 :
            break
        # 예산에 딱 맞은 경우 cnt ++ 하고 break
        elif B == price_sum :
            cnt += 1
            break
        else :
            cnt += 1


    max_cnt = max(max_cnt, cnt)

print(max_cnt)    
            
        


        
