N, M, K = map(int, input().split())

moves = list(map(int, input().split()))

positions_arr = [ 0 for _ in range(K) ]
#prev_positions_arr = [ 0 for _ in range(K) ]
points_arr = [ 0 for _ in range(K) ]

def cal_points(points_arr) :
    points = 0
    for i in range(len(points_arr)) :
        points += points_arr[i]
    
    return points

def get_max_points(idx) :

    if idx == N :
        check = cal_points(points_arr)
        # print(points_arr)
        # print(positions_arr)
        # print(check)
        # print()
        return check

    max_points = 0
    for i in range(K) :
        # 말의 이동로직
        next_position = moves[idx] + positions_arr[i]

        if next_position >= M-1 and positions_arr[i] < M-1 :
            points_arr[i] = 1

        #prev_positions_arr[i] = positions_arr[i]
        positions_arr[i] = next_position
        
        #print(idx, "번째: ", i, positions_arr)
        max_points = max(max_points, get_max_points(idx+1))

        positions_arr[i] -= moves[idx]
        # print("벗어남", positions_arr)
        if points_arr[i] and positions_arr[i] < M-1:
            points_arr[i] = 0
    
    return max_points

ans = get_max_points(0)
print(ans)

