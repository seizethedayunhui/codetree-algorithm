# 범위에 대한 조건은 먼저 써주어야 함!

N = int(input())

max_range = float('-inf')

N_list = list()

for _ in range(N) :
    N_list.append(int(input()))


cnt = 1 # 초기화 자체를 1로 해줌
for i in range(N) :
    if i == 0 or (N_list[i] != N_list[i-1]) :
        if cnt > max_range :
            max_range = cnt
    else :
        cnt += 1

print(max_range)