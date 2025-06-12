N = int(input())

seats = [ int(n) for n in input() ]

max_dis = float('-inf')

# i, j 는 각각 추가된 사람이 앉은 좌석 번호
for i in range(N) :

    if seats[i] :
        continue
    
    seats[i] = 1

    for j in range(N) :

        if seats[j] :
            continue
        
        seats[j] = 1

        current_min_dis = float('inf')
        pick_seats = list()

        for k in range(N) :
            if seats[k] :
                pick_seats.append(k)
        
        # 가장 가까운 사람들의 거리를 구함
        for l in range(1, len(pick_seats)) :
            current_min_dis = min(current_min_dis, pick_seats[l]-pick_seats[l-1])

        # 가장 가까운 사람들의 거리 중에서 가장 큰 값을 구함
        max_dis = max(max_dis, current_min_dis)

        # 초기화
        seats[j] = 0
    # 초기화
    seats[i] = 0

print(max_dis)
