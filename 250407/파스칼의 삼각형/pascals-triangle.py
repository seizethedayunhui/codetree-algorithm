n = int(input())

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n 

mat = [ [ 0 for _ in range(n) ] for i in range(n) ]

for i in range(n) :
    for j in range(i+1) :
        if in_range(i-1, j-1) and in_range(i-1, j) :
            mat[i][j] = mat[i-1][j-1] + mat[i-1][j]
        else :
            mat[i][j] = 1

for i in range(n) :
    for j in range(i+1) :
        print(mat[i][j], end=" ")
    print()