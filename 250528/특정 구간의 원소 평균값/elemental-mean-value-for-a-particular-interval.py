N = int(input())
N_list = list(map(int, input().split()))

cnt = 0

for i in range(N) :
    for j in range(i, N) :

        interval = 0
        for k in range(i, j+1) :
            interval += N_list[k]

        interval_avg = interval / abs(j-i+1)
        if interval_avg in N_list[i:j+1] : 
            cnt += 1

print(cnt)
