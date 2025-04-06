n, m = map(int, input().split())

value = 1

num_arr = [ [ 0 for _ in range(m) ] for _ in range(n) ]

for i in range(n) :
    for j in range(m) :
        num_arr[i][j] = value
        value += 1

for row in num_arr :
    for col in row :
        print(col, end=" ")
    print()