N = int(input())

records = [ int(elem) for elem in input() ]


max_dis = float('-inf')

for i in range(N) :

    if records[i] :
        continue

    # 해당 위체 학생을 넣는 경우 가정 -> 원소 값을 1로 변경
    records[i] = 1
    current_min_dis = float('inf')

    # 각 원소들과의 가장 가까운 거리를 구하는 과정
    for j in range(N) :

        if records[j] :

            for k in range(j+1, N) :
                if records[k] :
                    current_dis = abs(k-j)
                    current_min_dis = min(current_min_dis, current_dis)
            

    # 가장 가까이에 있는 학생들의 거리 중 가장 멀게 있는 것을 선택함. 
    max_dis = max(max_dis, current_min_dis)

    # 다시 값을 초기화
    records[i] = 0

print(max_dis)

        