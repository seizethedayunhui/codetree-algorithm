N = int(input())

points = list()

for _ in range(N) :
    x1, x2 = map(int ,input().split())
    points.append((x1, x2))

cnt = 0

for i in range(N) :

    overlap_flag = False

    # 겹치는 조건은
    # 기울기가 크고, 시작과 끝의 범위가 내 안에 있을 때

    for j in range(N) :

        if i == j :
            continue

        if (points[j][1] - points[j][0]) < (points[i][1] - points[i][0]) and points[j][0] >= points[i][0] and points[j][1] <= points[i][1] :
            overlap_flag = True

        if (points[j][1] - points[j][0]) > (points[i][1] - points[i][0]) and points[j][0] <= points[i][0] and points[j][1] >= points[i][1] :
            overlap_flag = True            

        if overlap_flag :
            break

    if not overlap_flag :
        cnt += 1

print(cnt)

        