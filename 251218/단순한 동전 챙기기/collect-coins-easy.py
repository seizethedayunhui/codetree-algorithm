import sys
sys.setrecursionlimit(10 ** 8)
MAX_INT = sys.maxsize

N = int(input())

mat = []
record = [ [ 0 for _ in range(N) ] for _ in range(N) ]

for _ in range(N):
    row = list()
    for e in input() :
        if e == "." :
            row.append(0)
        elif e == "S" :
            row.append(-1)
        elif e == "E":
            row.append(-2)
        else :
            element = int(e)
            row.append(element)
    mat.append(row)

points = list()
for i in range(N) :
    for j in range(N) :
        if mat[i][j] == - 1 :
            start_x = i
            start_y = j
        elif mat[i][j] == -2 :
            end_x = i
            end_y = j
        elif mat[i][j] :
            point = (i, j, mat[i][j])
            points.append(point)

# 오름차순으로 정렬
points.sort(lambda x : x[2])

def cal_dis(select_points) :

    dis = 0
    x = start_x
    y = start_y

    for i in range(len(select_points)) :

        nx = select_points[i][0]
        ny = select_points[i][1]
        dis += abs(x-nx) + abs(y-ny)
        x = nx
        y = ny

    dis += abs(end_x - x) + abs(end_y - y)

    return dis

select_points = list()

def find_min_moves(idx, cnt) :

    if cnt == 3 :
        return cal_dis(select_points)
    
    if idx == len(points) :
        return MAX_INT
    
    min_move = MAX_INT

    for i in range(idx, len(points)) :

        select_points.append((points[i][0], points[i][1]))
        min_move = min(min_move, find_min_moves(i+1, cnt+1))
        select_points.pop()

        min_move = min(min_move, find_min_moves(i+1, cnt))

    return min_move

ans = find_min_moves(0, 0)

if ans == MAX_INT :
    print(-1)
else :
    print(ans)



        




