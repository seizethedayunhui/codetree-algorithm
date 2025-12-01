N = int(input())

mat = [ list(map(int, input().split())) for _ in range(N) ]
record = [ [ 0 for _ in range(N) ] for _ in range(N) ]

points = []
for x in range(N) :
    for y in range(N) :
        if mat[x][y] :
            point = [x , y]
            points.append(point)
            record[x][y] = 1

def in_range(x, y) :
    return 0 <= x < N and 0 <= y < N

def record_bombs(i, point) :

    if i == 0 :
        dx = [ -2, -1, +1, +2 ]
        dy = [ 0, 0, 0, 0 ]

    elif i == 1 :
        dx = [ 0, 1, 0, -1]
        dy = [ 1, 0, -1, 0]

    else :
        dx = [ -1, 1, 1, -1]
        dy = [ 1, 1, -1 , -1]

    for j in range(4) :

        nx = point[0] + dx[j]
        ny = point[1] + dy[j]

        if in_range(nx, ny) :
            record[nx][ny] += 1


def remove_bombs(i, point) :

    if i == 0 :
        dx = [ -2, -1, +1, +2 ]
        dy = [ 0, 0, 0, 0 ]

    elif i == 1 :
        dx = [ 0, 1, 0, -1]
        dy = [ 1, 0, -1, 0]

    else :
        dx = [ -1, 1, 1, -1]
        dy = [ 1, 1, -1 , -1]
    
    for j in range(4) :

        nx = point[0] + dx[j]
        ny = point[1] + dy[j]

        if in_range(nx, ny) :
            record[nx][ny] -= 1

max_bombs = 0

def update_answer() :

    current_bombs = 0
    for i in range(N) :
        for j in range(N) :
            if record[i][j] :
                current_bombs += 1
    
    return current_bombs

def cnt_bombs(idx) :

    if idx == len(points) :
        # for x in range(N) :
        #     for y in range(N) :
        #         print(record[x][y], end=" ")
        #     print()
        # print()
        return update_answer()

    best = 0
    for i in range(3) :
        # bomb count
        record_bombs(i, points[idx])
        best = max(best, cnt_bombs(idx+1))
        remove_bombs(i, points[idx])

    return best

ans = cnt_bombs(0)

print(ans)