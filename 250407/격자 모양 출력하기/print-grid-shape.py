N, M = map(int, input().split())

mat = [ [ 0 for _ in range(N) ] for _ in range(N) ]

for _ in range(M) :
    r,c = map(int, input().split())
    mat[r-1][c-1] = r * c

for i in range(N) :
    for j in range(N) :
        print(mat[i][j], end=" ")
    print()