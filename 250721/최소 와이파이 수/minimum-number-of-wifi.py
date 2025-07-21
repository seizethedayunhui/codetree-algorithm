n, m = map(int, input().split())

arr = list(map(int, input().split()))

start_point = 0
cnt = 0


while (start_point < n) :

    not_available = True
    # 완벽한 스타트 포인트 결정
    for i in range(start_point, n) :
        if arr[i] :
            not_available = False
            start_point = i
            break

    # 해당 값이 0인 경우 사람이 살지 않기 때문에 굳이 와이파이를 설치할 필요가 없음. 
    if not not_available :
        cnt += 1

    next_point = start_point + (2 * m  + 1)
    start_point = next_point



print(cnt)
