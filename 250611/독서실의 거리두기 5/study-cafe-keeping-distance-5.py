N = int(input())

records = [ int(elem) for elem in input() ]


max_dis = float('-inf')

for i in range(N) :

    if records[i] :
        continue

    current_min_dis = float('inf')

    # 가장 가까이에 있는 학생들의 거리를 구함
    for k in range(N) :
        if k == i :
            continue

        if records[k] :
            current_dis = abs(i-k)
            current_min_dis = min(current_min_dis, current_dis)

    # 가장 가까이에 있는 학생들의 거리 중 가장 멀게 있는 것을 선택함. 
    max_dis = max(max_dis, current_min_dis)

print(max_dis)

        