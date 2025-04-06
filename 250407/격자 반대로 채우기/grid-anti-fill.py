N = int(input())

num = 1

new_mat = [ [ 0 for _ in range(N)] for _ in range(N) ]

for col in range(-1, -N-1, -1) :
    if abs(col) % 2 :

         for row in range(N-1, -1, -1) :
            new_mat[row][col] = num
            num += 1

    else :
        for row in range(N) :
            new_mat[row][col]= num
            num += 1

for row in new_mat :
    for col in row :
        print(col, end=" ")
    print()