num_list = list(map(int, input().split()))
cnt_arr = [ 0 for _ in range(6) ]

for num in num_list :
    cnt_arr[num-1] += 1

for i in range(6):
    print(f"{i+1} - {cnt_arr[i]}")