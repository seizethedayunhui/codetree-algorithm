num_arr = [ list(map(int, input().split())) for _ in range(2) ]
all_sum = 0

# 가로 평균
for num_list in num_arr :
    row_sum = 0
    for num in num_list :
        row_sum += num
        all_sum += num
    row_avg = row_sum / 4
    print(f"{row_avg:.1f}", end=" ")
print()

# 세로 평균
for j in range(4) :
    col_sum = 0
    for i in range(2) :
        col_sum += num_arr[i][j]
    col_avg = col_sum / 2
    print(f"{col_avg:.1f}", end=" ")
print()

avg = all_sum / 8
print(f"{avg:.1f}")