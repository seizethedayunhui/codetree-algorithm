n, m = map(int, input().split())

arr = list(map(int, input().split()))

start_point = 0
cnt = 0

while (start_point < n) :

    # 완벽한 스타트 포인트 결정
    for i in range(start_point, n) :
        if arr[i] :
            start_point = i
            break

    cnt += 1

    next_point = start_point + (2 * m  + 1)
    start_point = next_point



print(cnt)
