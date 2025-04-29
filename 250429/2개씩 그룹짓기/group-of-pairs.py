N = int(input())

N_list = list(map(int, input().split()))

sum_max_min = float('inf')

for i in range(2) :

    sum_max = float('-inf')

    for j in range(i, N, 2) :
        if j+1 >= N :
            current_max = N_list[j] + N_list[0]
        else :
            current_max = N_list[j] + N_list[j+1]

        if current_max > sum_max :
            sum_max = current_max

    if sum_max < sum_max_min :
        sum_max_min = sum_max

print(sum_max_min)
