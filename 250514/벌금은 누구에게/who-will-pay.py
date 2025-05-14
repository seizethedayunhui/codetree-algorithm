N, M, K = map(int, input().split())

cnt_list = [ 0 for _ in range(N) ]

ans = -1

for _ in range(M) :
    num = int(input())
    cnt_list[num-1] += 1
    if cnt_list[num-1] >= K :
        ans = num
        break

print(ans)

