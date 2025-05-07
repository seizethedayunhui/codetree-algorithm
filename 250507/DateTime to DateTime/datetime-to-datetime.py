A, B, C = map(int, input().split())

cnt = 0

d, h, m = 11, 11, 11

while True:
    # 만약 주어진 시간이 더 이전인 경우
    if A <= 11 :
        if B < 11 :
            if C < 11 :
                print(-1)
                break

    # 주어진 날짜, 시, 분에 도착한 경우
    if (d == A and h == B and m == C):
        print(cnt)
        break

    # m 범위를 벗어난 경우 reset, h +1
    if m >= 60 :
        m = 0
        h += 1
    
    # h 범위를 벗어난 경우 reset, d+1
    if h >= 24 :
        h = 0
        d += 1

    cnt += 1
    m += 1


    