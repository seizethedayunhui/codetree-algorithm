N = 5
mat = [ [ 0 for _ in range(N) ] for _ in range(N) ]

for i in range(5) :
    for j in range(5) :
        if not i :
            mat[i][j] = 1
        else :
            mat[i][j] = mat[i-1][j] + mat[i][j-1]

for row in mat :
    for col in row :
        print(col, end=" ")
    print()