N = int(input())
check_point = list()

for _ in range(N) :
    x, y = map(int, input().split())
    check_point.append((x,y))

min_distance = float('inf')
for i in range(1, N-1) :

    skip_point = i
    current_distance = 0

    for j in range(N-1) :
        if j == skip_point :
            continue
        # 스킵포인트 보다 한칸 앞의 포인트
        elif j == skip_point - 1 :
            current_distance += (
                abs( check_point[j][0]-check_point[j+2][0]) + abs(check_point[j][1]-check_point[j+2][1])
            )
        else :
           current_distance += (
                abs( check_point[j][0]-check_point[j+1][0]) + abs(check_point[j][1]-check_point[j+1][1])
            )

    min_distance = min(min_distance, current_distance)

print(min_distance)
        
