class Point:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

N = int(input())

Point_list = list()

for i in range(N):

    x, y = map(int, input().split())
    Point_list.append(Point(x, y, i+1))

Point_list.sort(key = lambda x : (abs(x.x-0)+abs(x.y-0), x.n))

for point in Point_list:
    print(point.n)

