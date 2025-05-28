N, M = map(int, input().split())

# 수열 입력 받음
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()

cnt = 0

for i in range( N - M + 1 ):

    cmp_list = list()   
    flag = True 
    for j in range(i, i+M) :
        cmp_list.append(A[j])

    cmp_list.sort()

    for k in range(M) :
        if cmp_list[k] != B[k] :
            flag = False
            break
    if flag :
        cnt += 1

print(cnt)
