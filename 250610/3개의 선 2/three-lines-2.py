N = int(input())
points = list()

for _ in range(N) :
    point = tuple(map(int, input().split()))
    points.append(point)

cnt = 0
for i in range(11) :
    for j in range(11) :
        for k in range(11) :


            # 1. 모두 x축에 평행한 경우
            cnt1 = 0
            flag1 = False
            for point in points:
                if point[1] == i or point[1] == j or point[1] == k :
                    cnt1 += 1
            if cnt1 == N :
                flag1 = True

            # 2. 모두 y축에 평행한 경우
            cnt2 = 0
            flag2 = False
            for point in points :
                if point[0] == i or point[0] == j or point[0] == k :
                    cnt2 += 1
            if cnt2 == N :
                flag2 = True

            # 3. x축에 평행한 것 1개, y축에 평행한 것 2개
            cnt3 = 0
            flag3 = False
            for point in points :
                if point[1] == i or point[0] == j or point[0] == k :
                    cnt3 += 1
            if cnt3 == N :
                flag3 = True

            # 4. y축에 평행한 것 1개, x축에 평행한 것 2개
            cnt4 = 0
            flag4 = False
            for point in points :
                if point[0] == i or point[1] == j or point[1] == k :
                    cnt4 += 1
            if cnt4 == N :
                flag4 = True

            if flag1 or flag2 or flag3 or flag4 :
                cnt += 1

if cnt :
    print(1)
else :
    print(0)

            
            