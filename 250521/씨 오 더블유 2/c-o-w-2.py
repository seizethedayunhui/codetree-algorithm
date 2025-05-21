N = int(input())

N_str = input()
N_list = list()

for elem in N_str:
    N_list.append(elem)

cnt = 0
for i in range(N) :
    for j in range(i+1, N):
        for k in range(j+1, N) :

            if N_list[i] == "C" and N_list[j] == "O" and N_list[k] == "W" :
                cnt += 1

print(cnt)