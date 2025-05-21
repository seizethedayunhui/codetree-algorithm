N = int(input())
N_list = list(map(int, input().split()))

max_sum = float('-inf')


for i in range(N-2) :
    for j in range(i+2,N) :
        max_sum = max(max_sum, N_list[i]+N_list[j])

print(max_sum)
        