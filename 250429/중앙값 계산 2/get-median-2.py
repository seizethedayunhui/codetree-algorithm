N = int(input())

N_list = list(map(int, input().split()))

for i in range(N) :
    if i % 2 == 0 :
        new_N_list = N_list[:i+1]
        new_N_list.sort()
        print(new_N_list[i//2], end=" ")
