arr1 = [ list(map(int, input().split())) for _ in range(3) ]
blank = input()
arr2 = [ list(map(int, input().split())) for _ in range(3) ]

new_mat = [[ 0 for _ in range(3) ] for _ in range(3) ]

for i in range(3) :
    for j in range(3) :
        new_mat[i][j] = arr1[i][j] * arr2[i][j]

for row in new_mat :
    for col in row :
        print(col, end=" ")
    print()