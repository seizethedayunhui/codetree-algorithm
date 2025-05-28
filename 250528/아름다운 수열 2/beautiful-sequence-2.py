N, M = map(int, input().split())

# 수열 입력 받음
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0

for i in range( N - M + 1 ):
    flag = True
    for j in range(i, i + M) :
        if A[j] not in B :
            flag = False
            break
    if flag :
        cnt += 1

print(cnt)
