N = int(input())

mat = [[ 0 for _ in range(N)] for _ in range(N) ]

for i in range(N) :
    for j in range(N) :
        if not i :
            mat[i][j] = 1
        elif not j :
            mat[i][j] = 1
        else :
            mat[i][j] = mat[i-1][j] + mat[i-1][j-1] + mat[i][j-1] # 격자의 바로위, 왼쪽위, 옆의 값의 합

for i in range(N) :
    for j in range(N) :
        print(mat[i][j], end=" ")
    print()