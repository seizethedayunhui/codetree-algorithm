N = int(input())

num_list = list(map(int, input().split()))

# 등차수열을 이루게 하는 것!
cnt = 0
for K in range(1, 101) :

    for i in range(N) :
        for j in range(i+1, N) :

            if K - num_list[i] == num_list[j] - K :
                cnt += 1

print(cnt)

           
