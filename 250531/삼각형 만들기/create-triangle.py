N = int(input())
points = list()

for _ in range(N) :
    x, y = map(int, input().split())
    points.append((x, y))

max_traingle = 0

for i in range(N) :
    for j in range(N) :
        for k in range(N) :

            if i == j or j == k or k == i :
                continue

            # 한 변은 x 축에 평행 & 다른 한 변은 y 축게 평행
            if points[i][0] == points[j][0] and points[j][1] == points[k][1] :

                # print(points[i], points[j], points[k])

                triangle = abs(points[i][1] - points[j][1]) * abs(points[j][0] - points[k][0])

                max_traingle = max(max_traingle, triangle)
                # print(max_traingle)

print(max_traingle)



