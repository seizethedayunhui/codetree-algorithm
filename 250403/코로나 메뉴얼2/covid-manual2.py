cnt_arr = [ 0 for _ in range(4) ]

for i in range(3) :

    flag, temp = input().split()
    temp = int(temp)

    if flag == 'Y':
        if temp >= 37 :
            cnt_arr[0] += 1
        else :
            cnt_arr[2] += 1
    else :
        if temp >= 37 :
            cnt_arr[1] += 1
        else :
            cnt_arr[3] += 1
        

for cnt in cnt_arr :
    print(cnt, end=" ")

if cnt_arr[0] >= 2 :
    print('E')
    