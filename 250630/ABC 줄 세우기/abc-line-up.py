N = int(input())

arr = list(map(ord, input().split()))

cnt = 0

# 처음부터 끝까지 loop
for i in range(N) :

    # 최소 change 횟수를 찾아야함
    # 따라서, 정렬되지 않는 부분의 min_num과 그 idx를 저장
    min_num = arr[i]
    point = i

    # min_num이랑 위치 찾음.
    for j in range(i+1, N) :

        if arr[j] < min_num :
            min_num = arr[j]
            point = j

    # 현재 수가 정렬되지 않은 부분에서 min_num이 아닌 경우
    if point != i :

        # 카운팅을 하기 위해서 버블정렬 사용
        for k in range(point, i, -1) :

            cnt += 1 # 카운트

            temp = arr[k]
            arr[k] = arr[k-1]
            arr[k-1] = temp

print(cnt)



