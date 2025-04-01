N = int(input())

for i in range(1, N+1) :
    measure_cnt = 0
    for j in range(1, i+1):
        if i % j == 0 :
            measure_cnt += 1
    # 소수는 약수가 2개
    if measure_cnt == 2:
        print(i, end=" ")