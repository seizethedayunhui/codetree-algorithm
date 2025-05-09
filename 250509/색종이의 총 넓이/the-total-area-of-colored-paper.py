N = int(input())

mat = [ [ 0 for _ in range(201)] for _ in range(201) ]

points = list()

for _ in range(N) :
    # 포인트 추가
    point = tuple(map(int, input().split()))
    points.append(point)

for point in points :

    for i in range(8) :
        for j in range(8) :
            # 어떻게 추가하나
            mat[100 + point[0]+i][100 + point[1]+j] += 1

cnt = 0

for row in mat :
    for col in row :
        if col >= 1 :
             cnt += 1

print(cnt)