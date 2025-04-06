n = int(input())

num = 1
new_mat = [ [ 0 for _ in range(n) ] for _ in range(n) ]
# 열 기준으로 써내려가기
for col in range(n) :
    for row in range(n) :
        new_mat[row][col] = num
        num += 1

for row in new_mat :
    for col in row :
        print(col, end=" ")
    print()