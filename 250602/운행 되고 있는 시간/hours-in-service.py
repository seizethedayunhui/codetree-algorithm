N = int(input())
times = list()

for _ in range(N) :
    time = tuple(map(int, input().split()))
    times.append(time)

max_time = float('-inf')


for i in range(N) :

    cnt_list = [ 0 for _ in range(1001) ]
    total_time = 0
    
    for j in range(N) :

        if i == j :
            continue

        for k in range(times[j][0], times[j][1]) :
            cnt_list[k] += 1


    for cnt in cnt_list :
        if cnt >= 1 :
            total_time += 1

    max_time = max(max_time, total_time)

print(max_time)

    

        