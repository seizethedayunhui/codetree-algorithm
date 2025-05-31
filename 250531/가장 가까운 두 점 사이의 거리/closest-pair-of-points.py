N = int(input())
points = list()

for _ in range(N) :

    x, y = map(int, input().split())

    points.append((x, y))

min_dis = float('inf')

for i in range(N) :
    for j in range(i+1, N) :

        distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2

        min_dis = min(min_dis, distance)

print(min_dis)
