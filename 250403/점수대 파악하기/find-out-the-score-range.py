score_list = list(map(int, input().split()))
cnt_arr = [ 0 for _ in range(10) ]

for score in score_list :
    
    if not score :
        break

    standard = int(score // 10)
    if not standard :
        continue
    
    cnt_arr[standard - 1] += 1

for i in range(9, -1, -1) :
    print(f"{(i+1)*10} - {cnt_arr[i]}")