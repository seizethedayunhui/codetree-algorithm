n, m = map(int, input().split())

mat = [ [ 0 for _ in range(n) ] for _ in range(n) ]

for _ in range(m) :
    r, c = map(int, input().split())

    # mat가 0,0 부터 시작하기 때문에 저장 시에 행과 열에 각각 -1
    mat[r-1][c-1] = 1

for row in mat :
    for col in row :
        print(col, end=" ")
    print()
