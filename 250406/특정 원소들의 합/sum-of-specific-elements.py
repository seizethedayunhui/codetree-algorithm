num_arr = [ list(map(int, input().split())) for _ in range(4) ]

num_sum = 0
for i in range(4) :
    for j in range(i+1) :
        num_sum += num_arr[i][j]

print(num_sum)