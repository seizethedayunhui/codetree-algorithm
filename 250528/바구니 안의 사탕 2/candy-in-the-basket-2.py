N, K = map(int, input().split())

N_cnt = [ 0 for _ in range(401) ]

for _ in range(N) :
    candy, l = map(int, input().split())

    # 같은 위치에 바구니가 있을 수도 있음!
    N_cnt[l] += candy


max_sum = float('-inf')
for i in range(K , 401 - K) :

    interal_sum = 0
    for j in range(i-K, i + K+1):
        interal_sum += N_cnt[j]
    max_sum = max(max_sum, interal_sum)

print(max_sum)
    