N, K = map(int, input().split())

num_list = list()
for _ in range(N) :
    num_list.append(int(input()))

max_cnt = float('-inf')
for i in range(N) :
    # i == 최솟값의 인덱스
    current_cnt = 0

    for j in range(N) :

        # i를 최솟값의 인덱스라고 잡았기 때문에 i 인덱스에 해당하는 값이 j 인덱스에 해당하는 값보다 큰지 확인해야함. 
        if num_list[j] >= num_list[i] and num_list[j]-num_list[i] <= K :
            current_cnt += 1

    max_cnt = max(max_cnt, current_cnt)

print(max_cnt)
