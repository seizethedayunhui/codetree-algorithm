N = int(input())

arr = list(map(int, input().split()))

cnt = 0
min_num = float('inf')

for i in range(N) :

    if arr[i] < min_num :
        min_num = arr[i]

second_num = float('inf')
second_idx = -1

for j in range(N) :

    if arr[j] == second_num :
        cnt += 1

    if arr[j] > min_num and arr[j] < second_num :
        second_num = arr[j]
        second_idx = j

# 두번째로 큰 수가 여러 개인 경우 & 두번째로 큰 수 자체가 존재하지 않는 경우
if cnt or (second_idx < 0) :
    print(-1)
else :
    print(second_idx + 1)





        

