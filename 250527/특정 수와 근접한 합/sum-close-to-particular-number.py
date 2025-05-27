N, S = map(int, input().split())
N_list = list(map(int, input().split()))

ans = S

# 제외 시킬 숫자 결정
for i in range(N) :
    for j in range(i+1, N) :
        cnt = 0
        for k in range(N) :
            if i != k and j != k :
                cnt += N_list[k]

        if abs(S-cnt) < ans :
            ans = abs(S-cnt)

print(ans)


