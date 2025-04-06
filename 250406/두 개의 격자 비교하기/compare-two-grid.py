N, M = map(int, input().split())

mat1 = [ list( map(int, input().split())) for _ in range(N) ]
mat2 = [ list( map(int ,input().split())) for _ in range(N) ]

new_mat = [ [ 1 for _ in range(M) ] for _ in range(N) ]

for i in range(N) :
    for j in range(M) :
        if mat1[i][j] == mat2[i][j] :
            new_mat[i][j] = 0

for row in new_mat :
    for col in row :
        print(col, end=" ")
    print()