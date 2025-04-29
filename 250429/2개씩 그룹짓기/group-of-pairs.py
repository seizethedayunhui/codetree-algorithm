N = int(input())

N_list = list(map(int, input().split()))

N_list.sort()

sum_max = float('-inf')

for i in range(N) :

    current_sum = N_list[i] + N_list[ 2*N-(i+1) ]

    if current_sum > sum_max :
        sum_max = current_sum

print(sum_max)
