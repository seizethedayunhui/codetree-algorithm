N = int(input())

N_list = list()

for _ in range(N) :
    N_list.append(int(input()))


max_len = float('-inf')

for i in range(N) :

    flag = N_list[i] + N_list[i-1]

    if i == 0 :
        cnt = 1

    elif ( N_list[i] < 0 and N_list[i] < flag ) or ( N_list[i] > 0 and N_list[i] > flag ) :
        if cnt > max_len :
            max_len = cnt
        cnt = 1

    else :
        cnt += 1
    


print(max_len)
