# 범위에 대한 조건은 먼저 써주어야 함!

N = int(input())

max_range = float('-inf')

N_list = list()

for _ in range(N) :
    N_list.append(int(input()))


cnt = 1 # 초기화 자체를 1로 해줌
for i in range(N) :
    if i == 0 or (N_list[i] != N_list[i-1]) :
        cnt = 1
    else :
        cnt += 1
    # 리스트의 last 원소까지 세어야 하는 경우가 있을 수도 있기 때문에
    # 중첩 if 문이 아니라, 각각의 if문으로 처리
    if cnt > max_range :
        max_range = cnt

print(max_range)