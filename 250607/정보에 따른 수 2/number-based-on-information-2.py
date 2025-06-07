T, a, b = map(int, input().split())

points = list()

for _ in range(T) :

    alpha, d = input().split()
    d = int(d)
    points.append((alpha, d))

cnt = 0
for i in range(a, b+1) :

    d1_min = float('inf')
    d2_min = float('inf')

    for point in points :

        if point[0] == 'S' :
            d1_min = min(d1_min, abs(i-point[1]))
        if point[0] == 'N' :
            d2_min = min(d2_min, abs(i-point[1]))

    if d1_min <= d2_min :
        cnt += 1

print(cnt)
