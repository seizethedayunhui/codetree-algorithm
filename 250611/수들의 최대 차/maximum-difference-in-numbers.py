N, K = map(int, input().split())

num_list = list()
for _ in range(N) :
    num_list.append(int(input()))

max_cnt = float('-inf')
for i in range(N) :
    # i == 최솟값의 인덱스
    current_cnt = 0
    
    for j in range(N) :
        if i == j :
            continue

        elif abs(num_list[i]-num_list[j]) <= K :
            current_cnt += 1

    max_cnt = max(max_cnt, current_cnt)

print(max_cnt)
