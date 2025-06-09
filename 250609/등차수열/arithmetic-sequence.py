N = int(input())

num_list = list(map(int, input().split()))

# 등차수열을 이루게 하는 것!
max_cnt = float('-inf')
for K in range(1, 101) :
    current_cnt = 0
    for i in range(N) :
        for j in range(i+1, N) :

            if K - num_list[i] == num_list[j] - K :
                current_cnt += 1
            
    max_cnt = max(max_cnt, current_cnt)

print(max_cnt)

           
