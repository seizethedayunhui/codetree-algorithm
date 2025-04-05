num_arr = [ list(map(int, input().split())) for _ in range(4) ]

for num_list in num_arr :
    num_sum = 0
    for num in num_list :
        num_sum += num
    print(num_sum)