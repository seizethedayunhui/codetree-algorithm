N = int(input())

A_info = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(i+1, N):
        if A_info[i] < A_info[j] :
            for k in range(j+1, N):
                if A_info[j] < A_info[k] :
                    cnt += 1

print(cnt)