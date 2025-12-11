N, M, K = map(int, input().split())

moves = list(map(int, input().split()))

positions_arr = [ 0 for _ in range(K) ]
points_arr = [ 0 for _ in range(K) ]

def cal_points(points_arr) :
    points = 0
    for i in range(len(points_arr)) :
        points += points_arr[i]
    
    return points

def get_max_points(idx) :

    if idx == N :
        check = cal_points(points_arr)
        return check

    max_points = 0
    for i in range(K) :
        # 말의 이동로직
        next_position = moves[idx] + positions_arr[i]

        # 처음으로 M 위치에 도착한 경우
        if next_position >= M-1 and positions_arr[i] < M-1 :
            points_arr[i] = 1

        positions_arr[i] = next_position
        
        max_points = max(max_points, get_max_points(idx+1))

        positions_arr[i] -= moves[idx]

        # 처음으로 M위치에 도달한 경우 원래대로 되돌려 주어야함. 
        if points_arr[i] and positions_arr[i] < M-1:
            points_arr[i] = 0
    
    return max_points

ans = get_max_points(0)
print(ans)

