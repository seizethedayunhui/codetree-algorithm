N, B = map(int, input().split())

records = list()

for _ in range(N) :

    record = tuple(map(int, input().split()))
    records.append(record)

records.sort( lambda x : x[0] + x[1] )


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

        # print(f"{i} {j+1}번 {price_sum}")
        # 예산 범위를 초과하는 경우 현재 것을 포함하지 않고 다음으로 넘어감.
        # 현재는 배송비, 선물 값이 따로 주어진 것이기 때문에 다음 것의 총합이 더 작아지는 경우가 발생할 수 있음. 
        if B - price_sum < 0 :
            price_sum -= records[j][1]

            if i == j :
                price_sum -= (records[j][0] // 2)
            else :
                price_sum -= records[j][0]

            continue
            
        # 예산을 만족하는 경우
        elif B == price_sum :
            cnt += 1
            break
        else :
            cnt += 1


    max_cnt = max(max_cnt, cnt)

print(max_cnt)    
            
        


        
