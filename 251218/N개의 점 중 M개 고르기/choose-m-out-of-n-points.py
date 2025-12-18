N, M = map(int, input().split())

MAX_VALUE = float('inf')

points = list()

for _ in range(N) :
    x, y = map(int, input().split())
    points.append((x,y))

select = list()

def find_max_dist() :

    max_dist = float('-inf')

    for i in range(M) :

        x1 = select[i][0]
        y1 = select[i][1]

        for j in range(i+1, M) :

            x2 = select[j][0]
            y2 = select[j][1]

            current_dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
            max_dist = max(max_dist, current_dist)
    
    return max_dist



def find_min_dist(idx) :

    if len(select) == M :
        current = find_max_dist()
        # print(current, select)
        return current
    
    if idx == N :
        return MAX_VALUE

    min_dist = MAX_VALUE

    for i in range(idx, N):

        select.append(points[i])
        min_dist = min(min_dist, find_min_dist(i+1))
        select.pop()

    return min_dist

ans = find_min_dist(0)
print(ans)   