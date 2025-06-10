N = int(input())
points = list()

for _ in range(N) :
    point = tuple(map(int, input().split()))
    points.append(point)

min_cnt = float('inf')
# x 값
for i in range(0, 101, 2) :
    # y 값
    for j in range(0, 101, 2) :

        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0

        for point in points :

            if point[0] > i and point[1] > j :
                cnt1 += 1
            elif point[0] < i and point[1] > j :
                cnt2 += 1
            elif point[0] < i and point[1] < j :
                cnt3 += 1
            else :
                cnt4 += 1
        
        if cnt1 >= cnt2 and cnt1 >= cnt3 and cnt1 >= cnt4 :
            current_cnt = cnt1
        elif cnt2 >= cnt1 and cnt2 >= cnt3 and cnt2 >= cnt4 :
            current_cnt = cnt2
        elif cnt3 >= cnt1 and cnt3 >= cnt2 and cnt3 >= cnt4 :
            current_cnt = cnt3
        else :
            current_cnt = cnt4

        min_cnt = min(min_cnt, current_cnt)

print(min_cnt)

        
            

