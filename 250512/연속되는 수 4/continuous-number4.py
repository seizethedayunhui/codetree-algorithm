N = int(input())

N_list = list()

for _ in range(N) :
    N_list.append(int(input()))

max_len = float('-inf')

for i in range(N) :

    if (i == 0) or (N_list[i] <= N_list[i-1]) :
        cnt = 1
    else :
        cnt += 1

    if cnt > max_len :
        max_len = cnt

print(max_len)
    